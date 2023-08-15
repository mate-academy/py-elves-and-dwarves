from __future__ import annotations
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for member in team:
        total_rating += member.get_rating()
    return total_rating


def elves_concert(elves: list[ElfRanger, Druid]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
