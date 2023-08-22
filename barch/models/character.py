"""Module for Character model."""

from __future__ import annotations
from typing import Any

from .base import BaseModel

import attrs

__all__ = ("Character", "Terrain", "TerrainDetails")


@attrs.define(init=False)
class Character(BaseModel):
    """Represents character model."""

    id: int

    name: str

    profile: str

    rarity: str

    base_star: int

    position: str

    role: str
    # TODO: check enums

    armor_type: str

    bullet_type: str

    weapon_type: str

    squad_type: str

    school: str

    terrain: Terrain


@attrs.define(init=False)
class Terrain(BaseModel):
    """"""

    urban: TerrainDetails

    outdoor: TerrainDetails

    indoor: TerrainDetails


@attrs.define
class TerrainDetails(BaseModel):
    """"""

    damage_dealt: str

    shield_block_rate: str
