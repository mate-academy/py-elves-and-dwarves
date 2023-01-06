from __future__ import annotations

from typing import Any, Generator

from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list[Elf]) -> Generator[None, Any, None]:
    return (elf.play_elf_song() for elf in elves)


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> Generator[None, Any, None]:
    return (dwarf.eat_favourite_dish() for dwarf in dwarves)
