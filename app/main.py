from __future__ import annotations
from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf_warrior import Dwarf


def calculate_team_total_rating(list_player: List[Player]) -> int:
    return sum(player.get_rating() for player in list_player)


def elves_concert(list_elf: List[Elf]) -> None:
    for elf in list_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarf: List[Dwarf]) -> None:
    for dwarf in list_dwarf:
        dwarf.eat_favourite_dish()
