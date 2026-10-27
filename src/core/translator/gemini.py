"""
Copyright (c) Cutleast
"""

from __future__ import annotations

import json
import time
from collections.abc import Callable
from typing import Any, override
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from core.config.translator_config import TranslatorConfig
from core.utilities.game_language import GameLanguage

from .translator import Translator


class GeminiTranslator(Translator):
    """Translator and contextual chat client for the Gemini Developer API."""

    API_URL = (
        "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    )
    DEFAULT_MODEL = "gemini-3.5-flash"
    REQUEST_TIMEOUT = 15
    MAX_RETRIES = 3
    MAX_RETRY_DELAY = 8
    RETRYABLE_STATUS_CODES = frozenset({429, 500, 502, 503, 504})

    def __init__(self, config: TranslatorConfig) -> None:
        """Validates that the Gemini API is configured."""

        super().__init__(config)
        if not config.gemini_api_key:
            raise RuntimeError("Gemini API key is required. Configure it in Settings.")

    @override
    def translate_uncached(self, text: str, dst: GameLanguage) -> str:
        instructions = self._config.gemini_custom_instructions.strip()
        system_instruction = (
            "You are a professional video game localization translator. "
            f"Translate from English into {dst.name}. Preserve the meaning, tone, "
            "markup, tags, variables, placeholders, line breaks, and control codes "
            "exactly. Do not translate proper names unless the custom instructions "
            "say otherwise. Return only the translated string, with no quotation "
            "marks or explanation."
        )
        if instructions:
            system_instruction += (
                f"\n\nUser's custom translation instructions:\n{instructions}"
            )

        return self.generate(
            system_instruction=system_instruction,
            contents=[{"role": "user", "parts": [{"text": text}]}],
        )

    def chat(
        self,
        *,
        original: str,
        current_translation: str,
        string_context: str,
        dst: GameLanguage,
        history: list[dict[str, Any]],
        on_retry: Callable[[str], None] | None = None,
    ) -> str:
        """Sends a contextual chat turn for the currently edited string."""

        custom_instructions = self._config.gemini_custom_instructions.strip()
        system_instruction = (
            "You are a localization assistant for a video game mod. Help the user "
            f"translate from English into {dst.name}. Keep markup, placeholders, "
            "variables, and line breaks intact. Treat the user's messages as a "
            "translation discussion. When asked for a translation, return the "
            "proposed string clearly and avoid changing unrelated context.\n\n"
            f"Record context: {string_context}\n"
            f"English source: {original}\n"
            f"Current translation: {current_translation or '(none)'}"
        )
        if custom_instructions:
            system_instruction += (
                "\n\nUser's custom translation instructions:\n" + custom_instructions
            )

        return self.generate(
            system_instruction=system_instruction,
            contents=history,
            on_retry=on_retry,
        )

    def generate(
        self,
        *,
        system_instruction: str,
        contents: list[dict[str, Any]],
        on_retry: Callable[[str], None] | None = None,
    ) -> str:
        """Calls Gemini's generateContent REST endpoint."""

        model = self._config.gemini_model.strip() or self.DEFAULT_MODEL
        url = self.API_URL.format(model=model)
        body = json.dumps(
            {
                "systemInstruction": {"parts": [{"text": system_instruction}]},
                "contents": contents,
                "generationConfig": {"temperature": 0.2},
            }
        ).encode("utf-8")
        for attempt in range(self.MAX_RETRIES + 1):
            request = Request(
                url,
                data=body,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "SSE-Translator/1.0",
                    "x-goog-api-key": self._config.gemini_api_key or "",
                },
                method="POST",
            )
            try:
                with urlopen(request, timeout=self.REQUEST_TIMEOUT) as response:
                    result = json.loads(response.read().decode("utf-8"))
                break
            except HTTPError as ex:
                detail = ex.read().decode("utf-8", errors="replace")
                if (
                    ex.code not in self.RETRYABLE_STATUS_CODES
                    or attempt >= self.MAX_RETRIES
                ):
                    raise RuntimeError(self._format_api_error(detail, ex.code)) from ex

                delay = self._get_retry_delay(ex.headers.get("Retry-After"), attempt)
                retry_message = (
                    f"Gemini API returned HTTP {ex.code}; retrying in {delay} second(s) "
                    f"({attempt + 1}/{self.MAX_RETRIES})."
                )
                self.log.warning(retry_message)
                if on_retry is not None:
                    on_retry(retry_message)
                time.sleep(delay)
            except URLError as ex:
                raise RuntimeError(
                    f"Could not connect to Gemini API: {ex.reason}"
                ) from ex
            except TimeoutError as ex:
                if attempt >= self.MAX_RETRIES:
                    raise RuntimeError(
                        "Gemini API request timed out after several retries."
                    ) from ex

                delay = self._get_retry_delay(None, attempt)
                retry_message = (
                    f"Gemini API request timed out; retrying in {delay} second(s) "
                    f"({attempt + 1}/{self.MAX_RETRIES})."
                )
                self.log.warning(retry_message)
                if on_retry is not None:
                    on_retry(retry_message)
                time.sleep(delay)
        else:
            raise RuntimeError("Gemini API request failed after several retries.")

        try:
            parts = result["candidates"][0]["content"]["parts"]
            text = "".join(part.get("text", "") for part in parts).strip()
        except (KeyError, IndexError, TypeError) as ex:
            prompt_feedback = result.get("promptFeedback", {})
            block_reason = prompt_feedback.get("blockReason")
            if block_reason:
                raise RuntimeError(
                    f"Gemini blocked this request: {block_reason}."
                ) from ex
            raise RuntimeError("Gemini returned an empty or invalid response.") from ex

        if not text:
            raise RuntimeError("Gemini returned an empty response.")
        return text

    @staticmethod
    def _format_api_error(detail: str, status_code: int) -> str:
        try:
            error = json.loads(detail).get("error", {})
            message = error.get("message")
        except (json.JSONDecodeError, AttributeError):
            message = None
        if message:
            return f"Gemini API error ({status_code}): {message}"
        return f"Gemini API request failed ({status_code})."

    @classmethod
    def _get_retry_delay(cls, retry_after: str | None, attempt: int) -> int:
        """Returns a bounded Retry-After delay or exponential backoff delay."""

        if retry_after:
            try:
                return min(max(0, int(retry_after)), cls.MAX_RETRY_DELAY)
            except ValueError:
                pass
        return min(2**attempt, cls.MAX_RETRY_DELAY)

    @override
    def get_cache_id(self, text: str, dst: GameLanguage) -> str:
        """Include model and custom instructions in the translation cache key."""

        return super().get_cache_id(
            f"{self._config.gemini_model}\n{self._config.gemini_custom_instructions}\n{text}",
            dst,
        )
