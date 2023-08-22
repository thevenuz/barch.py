"""This module has the client to connect to BlueArchive API."""

from __future__ import annotations
from barch import services, serializer

__all__ = ("Client",)


class Client:
    """An asynchronous client used to interact with the BlueArchive API."""

    __slots__ = ("_http", "_serializer", "_character")

    def __init__(self) -> None:
        self._http = services.HttpService()
        self._serializer = serializer.Serializer()
        self._character = services.CharacterService(self._http, self._serializer)

    @property
    def character(self) -> services.CharacterService:
        """"""
        return self._character

    async def close(self) -> None:
        """"""
        await self._http.close()
