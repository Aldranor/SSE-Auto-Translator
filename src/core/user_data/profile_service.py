"""
Copyright (c) Cutleast
"""

from pathlib import Path
from typing import Optional
from uuid import uuid4

from mod_manager_lib.core.mod_manager.modorganizer.instance_info import MO2InstanceInfo
from mod_manager_lib.core.mod_manager.vortex.profile_info import ProfileInfo
from pydantic import BaseModel, Field

from core.config.translator_config import TranslatorConfig
from core.config.user_config import UserConfig


class TranslationProfile(BaseModel):
    """Describes one modlist profile."""

    id: str
    """Stable identifier used for profile-specific storage."""

    name: str
    """Name displayed in the profile selector."""


class ProfileRegistry(BaseModel):
    """Stores available profiles and the currently selected profile."""

    active_profile_id: str = "default"
    """Identifier of the profile loaded at startup."""

    profiles: list[TranslationProfile] = Field(default_factory=list)
    """Profiles configured by the user."""


class ProfileService:
    """Manages modlist profiles and their isolated configuration directories."""

    DEFAULT_PROFILE_ID: str = "default"
    """Identifier reserved for the legacy shared data directory."""

    __data_path: Path
    __registry_path: Path
    __registry: ProfileRegistry

    def __init__(self, data_path: Path) -> None:
        """
        Args:
            data_path (Path): Shared application data directory.
        """

        self.__data_path = data_path
        self.__registry_path = data_path / "profiles.json"
        self.__registry = self.__load_registry()

    @property
    def profiles(self) -> list[TranslationProfile]:
        """Returns the configured profiles."""

        return self.__registry.profiles.copy()

    @property
    def active_profile(self) -> TranslationProfile:
        """Returns the profile selected for the current application run."""

        try:
            return next(
                profile
                for profile in self.__registry.profiles
                if profile.id == self.__registry.active_profile_id
            )
        except StopIteration as ex:
            raise ValueError(
                f"Active profile '{self.__registry.active_profile_id}' is unknown."
            ) from ex

    @property
    def active_data_path(self) -> Path:
        """Returns the active profile's configuration and cache directory."""

        return self.get_profile_data_path(self.__registry.active_profile_id)

    def get_profile_data_path(self, profile_id: str) -> Path:
        """Returns the data directory for a profile.

        Args:
            profile_id (str): Profile identifier.

        Returns:
            Path: Profile-specific data directory.

        Raises:
            ValueError: If the profile identifier is malformed.
        """

        if profile_id == ProfileService.DEFAULT_PROFILE_ID:
            return self.__data_path

        if len(profile_id) != 32 or any(
            character not in "0123456789abcdef" for character in profile_id.lower()
        ):
            raise ValueError(f"Invalid profile identifier '{profile_id}'.")

        return self.__data_path / "profiles" / profile_id

    def create_profile(
        self,
        name: str,
        mod_instance: Optional[MO2InstanceInfo | ProfileInfo],
        user_config: UserConfig,
        translator_config: TranslatorConfig,
    ) -> TranslationProfile:
        """Creates a profile with copied settings and shared translation storage.

        Args:
            name (str): Display name for the new profile.
            mod_instance (Optional[MO2InstanceInfo | ProfileInfo]): Modlist instance.
            user_config (UserConfig): Current user settings to copy.
            translator_config (TranslatorConfig): Current translator settings to copy.

        Returns:
            TranslationProfile: The newly created profile.

        Raises:
            ValueError: If the name is empty or already in use.
            OSError: If the profile directory cannot be created.
        """

        normalized_name: str = name.strip()
        if not normalized_name:
            raise ValueError("Profile name must not be empty.")
        if any(
            profile.name.casefold() == normalized_name.casefold()
            for profile in self.__registry.profiles
        ):
            raise ValueError(f"A profile named '{normalized_name}' already exists.")

        profile: TranslationProfile = TranslationProfile(
            id=uuid4().hex,
            name=normalized_name,
        )
        profile_path: Path = self.get_profile_data_path(profile.id)
        profile_path.mkdir(parents=True, exist_ok=False)

        # BaseConfig stores a ConfigManager callback in a private attribute. A deep
        # copy would try to pickle that QObject, so a shallow model copy is intentional
        # here: the copied models are only serialized and never edited afterward.
        new_user_config: UserConfig = user_config.model_copy(
            deep=False, update={"mod_instance": mod_instance}
        )
        self.__write_config(
            profile_path / UserConfig.get_config_name(), new_user_config
        )
        self.__write_config(
            profile_path / TranslatorConfig.get_config_name(),
            translator_config.model_copy(deep=False),
        )

        self.__registry.profiles.append(profile)
        self.__save_registry()
        return profile

    def set_active_profile(self, profile_id: str) -> None:
        """Selects the profile to load on the next application start.

        Args:
            profile_id (str): Profile identifier to activate.

        Raises:
            ValueError: If the identifier is not in the profile registry.
        """

        if not any(profile.id == profile_id for profile in self.__registry.profiles):
            raise ValueError(f"Unknown profile identifier '{profile_id}'.")

        self.__registry.active_profile_id = profile_id
        self.__save_registry()

    def rename_profile(self, profile_id: str, name: str) -> None:
        """Renames a profile without changing its stored data.

        Args:
            profile_id (str): Profile identifier to rename.
            name (str): New display name.

        Raises:
            ValueError: If the name is empty, already in use, or the ID is unknown.
        """

        normalized_name: str = name.strip()
        if not normalized_name:
            raise ValueError("Profile name must not be empty.")

        try:
            profile: TranslationProfile = next(
                profile
                for profile in self.__registry.profiles
                if profile.id == profile_id
            )
        except StopIteration as ex:
            raise ValueError(f"Unknown profile identifier '{profile_id}'.") from ex

        if any(
            other.id != profile_id
            and other.name.casefold() == normalized_name.casefold()
            for other in self.__registry.profiles
        ):
            raise ValueError(f"A profile named '{normalized_name}' already exists.")

        profile.name = normalized_name
        self.__save_registry()

    def __load_registry(self) -> ProfileRegistry:
        """Loads the registry and migrates existing data to the default profile."""

        if self.__registry_path.is_file():
            registry: ProfileRegistry = ProfileRegistry.model_validate_json(
                self.__registry_path.read_text(encoding="utf-8")
            )
        else:
            registry = ProfileRegistry()

        changed: bool = False
        if not any(
            profile.id == ProfileService.DEFAULT_PROFILE_ID
            for profile in registry.profiles
        ):
            registry.profiles.insert(
                0,
                TranslationProfile(
                    id=ProfileService.DEFAULT_PROFILE_ID,
                    name="Default",
                ),
            )
            changed = True

        if not any(
            profile.id == registry.active_profile_id for profile in registry.profiles
        ):
            registry.active_profile_id = ProfileService.DEFAULT_PROFILE_ID
            changed = True

        if changed or not self.__registry_path.is_file():
            self.__registry = registry
            self.__save_registry()

        return registry

    def __save_registry(self) -> None:
        """Writes the profile registry atomically."""

        self.__registry_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path: Path = self.__registry_path.with_suffix(".json.tmp")
        temporary_path.write_text(
            self.__registry.model_dump_json(indent=4), encoding="utf-8"
        )
        temporary_path.replace(self.__registry_path)

    @staticmethod
    def __write_config(path: Path, config: UserConfig | TranslatorConfig) -> None:
        """Writes a profile configuration file.

        Args:
            path (Path): Destination configuration file.
            config (UserConfig | TranslatorConfig): Configuration to serialize.
        """

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            config.model_dump_json(indent=4, by_alias=True, exclude_defaults=True),
            encoding="utf-8",
        )
