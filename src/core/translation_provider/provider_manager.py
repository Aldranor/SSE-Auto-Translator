"""
Copyright (c) Cutleast
"""

import logging
from typing import Literal, NoReturn, TypeVar, overload

from core.config.user_config import UserConfig

from .cdt_api.ctd_api import CDTApi
from .nm_api.nm_api import NexusModsApi
from .provider_api import ProviderApi
from .provider_preference import ProviderPreference
from .source import Source

T = TypeVar("T", bound=ProviderApi)


class ProviderManager:
    """
    Creates and resolves the translation providers configured for one application run.
    """

    __providers: dict[Source, ProviderApi]
    __on_demand_providers: dict[Source, ProviderApi]
    __provider_preference: ProviderPreference
    __user_config: UserConfig

    log: logging.Logger = logging.getLogger("ProviderManager")

    def __init__(self, user_config: UserConfig) -> None:
        """
        Initializes the configured providers.

        Args:
            user_config (UserConfig): The user configuration.
        """

        self.__providers = {}
        self.__on_demand_providers = {}
        self.__provider_preference = user_config.provider_preference
        self.__user_config = user_config

        self.log.info("Initializing configured translation providers.")
        self.log.debug(f"Provider preference: '{self.__provider_preference}'")

        for source in self.__get_configured_sources():
            self.__initialize_provider(source, user_config)

    @property
    def providers(self) -> tuple[ProviderApi, ...]:
        """
        Gets the initialized providers in configured preference order.

        Returns:
            tuple[ProviderApi, ...]: The configured providers.
        """

        return tuple(self.__providers.values())

    @property
    def has_providers(self) -> bool:
        """
        Checks whether at least one translation provider was initialized.

        Returns:
            bool: Whether at least one provider is available.
        """

        return bool(self.__providers)

    def is_source_available(self, source: Source) -> bool:
        """
        Checks whether a provider for a source was initialized.

        Args:
            source (Source): Source to check.

        Returns:
            bool: Whether a provider for the source is available.
        """

        return source in self.__providers

    def __get_configured_sources(self) -> tuple[Source, ...]:
        """
        Gets the sources configured by the user's provider preference.

        Returns:
            tuple[Source, ...]: Sources in preference order.
        """

        match self.__provider_preference:
            case ProviderPreference.OnlyNexusMods:
                return (Source.NexusMods,)
            case ProviderPreference.PreferNexusMods:
                return (Source.NexusMods, Source.Confrerie)
            case ProviderPreference.OnlyConfrerie:
                return (Source.Confrerie,)
            case ProviderPreference.PreferConfrerie:
                return (Source.Confrerie, Source.NexusMods)

    def __initialize_provider(self, source: Source, user_config: UserConfig) -> None:
        """
        Initializes one provider without preventing other configured sources from starting.

        Args:
            source (Source): Source to initialize.
            user_config (UserConfig): The user configuration.
        """

        try:
            provider: ProviderApi = self.__create_provider(source, user_config)
        except Exception:
            self.log.exception(f"Failed to initialize provider '{source}'.")

        else:
            self.__providers[source] = provider

    def get_default_provider(self) -> ProviderApi:
        """
        Gets the highest-priority initialized provider.

        Raises:
            ValueError: When no provider is initialized.

        Returns:
            ProviderApi: The default provider.
        """

        if self.__providers:
            return next(iter(self.__providers.values()))

        raise ValueError("No translation provider is initialized.")

    def get_provider(self, provider_type: type[T]) -> T:
        """
        Gets an initialized provider by implementation type.

        Args:
            provider_type (type[T]): Provider implementation type.

        Raises:
            ValueError: When no matching provider is initialized.

        Returns:
            T: The requested provider.
        """

        for provider in (
            *self.__providers.values(),
            *self.__on_demand_providers.values(),
        ):
            if isinstance(provider, provider_type):
                return provider

        raise ValueError(
            f"Provider of type '{provider_type.__name__}' is not initialized."
        )

    @overload
    def get_provider_by_source(self, source: Literal[Source.Local]) -> NoReturn: ...

    @overload
    def get_provider_by_source(
        self, source: Literal[Source.NexusMods]
    ) -> NexusModsApi: ...

    @overload
    def get_provider_by_source(self, source: Literal[Source.Confrerie]) -> CDTApi: ...

    def get_provider_by_source(self, source: Source) -> ProviderApi:
        """
        Gets a provider by source, creating it on demand if needed.

        Args:
            source (Source): Provider source.

        Raises:
            ValueError: When the source is local or unsupported.

        Returns:
            ProviderApi: The provider for the source.
        """

        if source is Source.Local:
            raise ValueError("Local files do not have a translation provider.")

        provider = self.__providers.get(source)
        if provider is not None:
            return provider

        provider = self.__on_demand_providers.get(source)
        if provider is not None:
            return provider

        provider = self.__create_provider(source, self.__user_config)
        self.__on_demand_providers[source] = provider
        self.log.info("Initialized provider '%s' on demand.", source)
        return provider

    def __create_provider(self, source: Source, user_config: UserConfig) -> ProviderApi:
        """Create a provider using the current user configuration.

        Args:
            source (Source): Provider to create.
            user_config (UserConfig): User configuration for credentials.

        Returns:
            ProviderApi: The newly created provider.
        """

        match source:
            case Source.NexusMods:
                provider = NexusModsApi()
                provider.set_api_key(user_config.api_key)
                provider.set_website_session(user_config.nexus_website_session)
                return provider

            case Source.Confrerie:
                return CDTApi()

            case _:
                raise ValueError(f"Unsupported translation provider source '{source}'.")
