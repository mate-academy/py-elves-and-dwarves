from __future__ import annotations
from typing import Optional

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: Optional[list[Player]]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elfs: Optional[list[Elf]]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Optional[list[Dwarf]]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
