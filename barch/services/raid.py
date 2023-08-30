"""Module for raid service."""

from __future__ import annotations
from typing import TypeVar

from .base import BaseService
from barch.result import Result, Success, Error
from barch.models import HttpSuccessResponse, HttpErrorResponse, Raids
from barch import endpoints


T = TypeVar("T")
ValueT = TypeVar("ValueT")
ResultT = Result[ValueT, HttpErrorResponse]

__all__ = ("RaidService",)


class RaidService(BaseService):
    """"""

    __slots__ = ()

    async def _get_raids(self, is_jp: bool = False) -> ResultT[list[Raids]]:
        """"""
        if is_jp:
            route = endpoints.GET_RAIDS_JP.generate_route()
        else:
            route = endpoints.GET_RAIDS.generate_route()
        result = await self._http.fetch(route)

        if isinstance(result, HttpErrorResponse):
            return Error(result)

        return Success(self._serializer.deserialize_raids(result.data))

    async def get_raids(self) -> ResultT[list[Raids]]:
        """"""

        return await self._get_raids()

    async def get_raids_jp(self) -> ResultT[list[Raids]]:
        """"""

        return await self._get_raids(is_jp=True)
