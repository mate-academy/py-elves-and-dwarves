from __future__ import annotations

from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(elf_player_class.get_rating() for elf_player_class in team)


def elves_concert(elves: list[ElfRanger | Druid]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(
        dwarves: list[DwarfWarrior | DwarfBlacksmith]
) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
