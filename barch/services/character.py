"""Moduke for character related services."""

from __future__ import annotations
from typing import TypeVar

from .base import BaseService
from barch.models import HttpErrorResponse, HttpSuccessResponse, Character
from barch import endpoints
from barch.result import Result, Success, Error


T = TypeVar("T")
ValueT = TypeVar("ValueT")
ResultT = Result[ValueT, HttpErrorResponse]

__all__ = ("CharacterService",)


class CharacterService(BaseService):
    """The service that handles all the methods related to characters."""

    __slots__ = ()

    async def get_all_characters(self) -> ResultT[list[Character]]:
        """Get all the characters with details."""

        route = endpoints.GET_ALL_CHARACTERS.generate_route()
        result = await self._http.fetch(route)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(
            [self._serializer.deserialize_character(element) for element in result.data]
        )
