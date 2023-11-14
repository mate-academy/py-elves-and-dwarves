from __future__ import annotations

from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf_renger import ElfRanger


def calculate_team_total_rating(team: list[ElfRanger]) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(elves: list[Elf]) -> None:
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
