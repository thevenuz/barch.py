"""Module to serialize and deserialize JSON data and models."""

from __future__ import annotations
from typing import TypeVar, Any

from barch.models import Character, Terrain, TerrainDetails


T = TypeVar("T")

__all__ = ("Serializer",)


class Serializer:
    """Deserializes JSON data to models."""

    __slots__ = ()

    def _to_camel_case(self, attr: str) -> str:
        """"""
        first, *rest = attr.split("_")
        return "".join((first.lower(), *map(str.title, rest)))

    def _set_attrs(
        self, model: Any, data: dict[str, Any], *attrs: str, camel_case: bool = False
    ) -> None:
        """Generate model from JSON payload."""

        if data:
            for attr in attrs:
                cased_attr = self._to_camel_case(attr) if camel_case else attr

                if data.get(cased_attr) is not None:
                    setattr(model, attr, data[cased_attr])
                else:
                    setattr(model, attr, None)

    def _set_attrs_cased(self, model: Any, data: dict[str, Any], *attrs: str) -> None:
        """"""
        return self._set_attrs(model, data, *attrs, camel_case=True)

    def _deserialize_terrain(self, data: dict[str, Any]) -> Terrain:
        """"""

        terrain = Terrain()

        terrain.urban = self._deserialize_terrain_details(data.get("urban", {}))
        terrain.outdoor = self._deserialize_terrain_details(data.get("outdoor", {}))
        terrain.indoor = self._deserialize_terrain_details(data.get("indoor", {}))

        return terrain

    def _deserialize_terrain_details(self, data: dict[str, Any]) -> TerrainDetails:
        """"""

        terrain_details = TerrainDetails(
            data.get("DamageDealt", ""), data.get("ShieldBlockRate", "")
        )

        return terrain_details

    def deserialize_character(self, data: dict[str, Any]) -> Character:
        """"""

        character = Character()

        character.terrain = self._deserialize_terrain(data.get("terrain", {}))

        self._set_attrs_cased(
            character,
            data,
            "id",
            "name",
            "profile",
            "rarity",
            "base_star",
            "position",
            "role",
            "armor_type",
            "bullet_type",
            "weapon_type",
            "squad_type",
            "school",
        )

        return character
