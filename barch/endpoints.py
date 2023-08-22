"""Module for endpoints used in the library."""

from __future__ import annotations
from typing import Final

from barch.models import Route

BASEURL: Final[str] = "https://api.ennead.cc/buruaka"

CHARACTERURL: Final[str] = f"{BASEURL}/character"
QUERYURL: Final[str] = f"{CHARACTERURL}/query?"
RAIDURL: Final[str] = f"{BASEURL}/raid"

JP_SUFFIX: Final[str] = f"?region=japan"

GET_ALL_CHARACTERS: Final[Route] = Route("GET", f"{CHARACTERURL}")
GET_ALL_CHARACTERS_JP: Final[Route] = Route("GET", f"{GET_ALL_CHARACTERS}{JP_SUFFIX}")

GET_CHARACTER: Final[str] = Route("GET", f"{CHARACTERURL}/()")
GET_CHARACTER_JP: Final[str] = Route("GET", f"{CHARACTERURL}/(){JP_SUFFIX}")

# GET_CHARACTER_BY_ROLE: Final[str] = f"{QUERYURL}role=()"
