"""Moduke for character related services."""

from __future__ import annotations
from typing import TypeVar

from .base import BaseService
from barch.models import (
    HttpErrorResponse,
    HttpSuccessResponse,
    Character,
    CharacterDetails,
    Characters,
)
from barch import endpoints
from barch.result import Result, Success, Error


T = TypeVar("T")
ValueT = TypeVar("ValueT")
ResultT = Result[ValueT, HttpErrorResponse]

__all__ = ("CharacterService",)


class CharacterService(BaseService):
    """The service that handles all the methods related to characters."""

    __slots__ = ()

    async def _get_all_characters(
        self, is_jp: bool = False
    ) -> ResultT[list[Character]]:
        """"""

        if is_jp:
            route = endpoints.GET_ALL_CHARACTERS_JP.generate_route()
        else:
            route = endpoints.GET_ALL_CHARACTERS.generate_route()

        result = await self._http.fetch(route)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(
            [self._serializer.deserialize_character(element) for element in result.data]
        )

    async def get_all_characters(self) -> ResultT[list[Character]]:
        """Get all the characters with details."""

        # route = endpoints.GET_ALL_CHARACTERS.generate_route()
        # result = await self._http.fetch(route)

        # if isinstance(result, HttpErrorResponse):
        #     return Error(result)

        # return Success(
        #     [self._serializer.deserialize_character(element) for element in result.data]
        # )

        return await self._get_all_characters()

    async def get_all_characters_jp(self) -> ResultT[list[Character]]:
        """"""

        # route = endpoints.GET_ALL_CHARACTERS_JP.generate_route()
        # result = await self._http.fetch(route)

        # if isinstance(result, HttpErrorResponse):
        #     return Error(result)

        # return Success(
        #     [self._serializer.deserialize_character(element) for element in result.data]
        # )

        return await self._get_all_characters(is_jp=True)

    async def _get_character(
        self, name: str | None = None, id: int | None = None, is_jp: bool = False
    ) -> ResultT[CharacterDetails]:
        """"""

        if id:
            params = {"id": "true"}

        if is_jp:
            route = endpoints.GET_CHARACTER_JP.generate_route(
                name if name else id
            ).with_params(params if params else None)

        else:
            route = endpoints.GET_CHARACTER.generate_route(
                name if name else id
            ).with_params(params if params else None)

        result = await self._http.fetch(route)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_character_details(result.data))

    async def get_character(
        self, name: str | None = None, id: int | None = None
    ) -> ResultT[CharacterDetails]:
        """"""

        if name or id:
            return await self._get_character(name=name, id=id)

        else:
            raise ValueError("Atleast one parameter must be specified.")

    async def get_character_jp(
        self, name: str | None = None, id: int | None = None
    ) -> ResultT[CharacterDetails]:
        """"""

        return await self._get_character(name=name, id=id, is_jp=True)

    async def get_character_by_query(
        self,
        role: str | None = None,
        type: str | None = None,
        school: str | None = None,
        club: str | None = None,
        position: str | None = None,
        weapon: str | None = None,
        damage: str | None = None,
        armor: str | None = None,
    ) -> ResultT[Characters]:
        """"""

        if any([role, type, school, club, position, weapon, damage, armor]):
            params = {
                "role": role if role else "",
                "type": type if type else "",
                "school": school if school else "",
                "club": club if club else "",
                "position": position if position else "",
                "weapon": weapon if weapon else "",
                "damage": damage if damage else "",
                "armor": armor if armor else "",
            }

            route = endpoints.GET_CHARACTER_QUERY.generate_route().with_params(params)
            result = await self._http.fetch(route)

            if isinstance(result, HttpErrorResponse):
                return Error(result)

            return Success(
                [
                    self._serializer.deserialize_characters_from_query(char)
                    for char in result.data
                ]
            )

        else:
            raise ValueError("Atleast one parameter must be specified.")
