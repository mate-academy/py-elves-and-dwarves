from __future__ import annotations
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(
        list_players: list[Druid | ElfRanger]
) -> int | float:
    return sum(player.get_rating() for player in list_players)


def elves_concert(list_elf: list[Druid | ElfRanger]) -> None:
    for elf in list_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(
        list_dwarf: list[DwarfWarrior | DwarfBlacksmith]
) -> None:
    for dwarf in list_dwarf:
        dwarf.eat_favourite_dish()
