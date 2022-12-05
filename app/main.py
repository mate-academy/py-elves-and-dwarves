from __future__ import annotations

from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players_team: list[ElfRanger,
                                                   Druid,
                                                   DwarfWarrior,
                                                   DwarfBlacksmith]) -> int:
    total_rating = 0
    for player in players_team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves_team: list[ElfRanger, Druid]) -> None:
    for elf in elves_team:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_team: list[DwarfWarrior,
                                           DwarfBlacksmith]) -> None:
    for dwarf in dwarfs_team:
        dwarf.eat_favourite_dish()
