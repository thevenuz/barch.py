"""Module for Character model."""

from __future__ import annotations
from typing import Any

from .base import BaseModel
from barch.enums import Position, Role, Rarity

import attrs

__all__ = (
    "Character",
    "Terrain",
    "BaseCharacter",
    "TerrainDetails",
    "CharacterInfo",
    "Image",
    "CharacterDetails",
    "Stats",
    "CommonModel",
    "Skills",
    "Characters",
)


@attrs.define(init=False)
class BaseCharacter(BaseModel):
    """Represents base character model."""

    name: str

    profile: str

    rarity: Rarity

    base_star: int

    position: Position

    role: Role

    armor_type: str

    bullet_type: str

    weapon_type: str

    squad_type: str


@attrs.define(init=False)
class Character(BaseCharacter):
    """Represents character model."""

    id: int

    # name: str

    # profile: str

    # rarity: Rarity

    # base_star: int

    # position: Position

    # role: Role
    # TODO: check enums

    # armor_type: str

    # bullet_type: str

    # weapon_type: str

    # squad_type: str

    school: str

    terrain: Terrain


@attrs.define(init=False)
class CharacterInfo(BaseModel):
    """"""

    age: int
    # TODO: string to int

    birth_date: str

    height: str

    artist: str

    club: str

    school: str

    school_year: str

    voice_actor: str


@attrs.define
class Image(BaseModel):
    """"""

    icon: str

    lobby: str

    portrait: str


@attrs.define(init=False)
class CharacterDetails(BaseModel):
    """"""

    id: int

    is_released: bool

    is_playable: bool

    character: BaseCharacter

    info: CharacterInfo

    image: Image

    stat: Stats

    terrain: Terrain

    skills: Skills


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


@attrs.define(init=False)
class Stats(BaseModel):
    """"""

    id: int

    attack_level1: int

    attack_level100: int

    max_hp_level1: int

    max_hp_level100: int

    defense_level1: int

    defense_level100: int

    heal_power_level1: int

    heal_power_level100: int

    def_penetrate_level1: int

    def_penetrate_level100: int

    ammo_count: int

    ammo_cost: int

    range: int

    move_speed: int

    street_mood: str

    outdoor_mood: str

    indoor_mood: str


@attrs.define
class CommonModel(BaseModel):
    """"""

    id: int

    name: str

    description: str


@attrs.define(init=False)
class Skills(BaseModel):
    """"""

    ex: list[CommonModel]

    normal: list[CommonModel]

    passive: list[CommonModel]

    sub: list[CommonModel]


@attrs.define
class Characters(BaseModel):
    """"""

    id: int

    name: str
