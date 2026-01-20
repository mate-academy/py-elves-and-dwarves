from __future__ import annotations

from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(
        teams: list[ElfRanger | Druid | DwarfWarrior | DwarfBlacksmith]
) -> int:
    return sum(player.get_rating() for player in teams)


def elves_concert(team_elf: list[ElfRanger | Druid]) -> None:
    for elf in team_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(
        team_dwarves: list[DwarfWarrior | DwarfBlacksmith]
) -> None:
    for dwarf in team_dwarves:
        dwarf.eat_favourite_dish()
