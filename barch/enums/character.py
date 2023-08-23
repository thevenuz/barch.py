"""Module for all the enums related to character."""

from __future__ import annotations

from .base import BaseEnum

__all__ = ("Position", "Role", "Rarity")


class Position(BaseEnum):
    """"""

    Back = "Back"

    Front = "Front"

    Middle = "Middle"


class Role(BaseEnum):
    """"""

    Dealer = "Dealer"

    Healer = "Healer"

    Support = "Support"

    Tank = "Tank"

    TacticalSupport = "T.S."


class Rarity(BaseEnum):
    """"""

    Rare = "R"

    SuperRare = "SR"

    SuperSuperRare = "SSR"
