from __future__ import annotations
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(list_of_team: list) -> int:
    return sum(member.get_rating() for member in list_of_team)


def elves_concert(list_of_elfs: list[ElfRanger, Druid]) -> None:
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarf: list[Dwarf]) -> None:
    for member in list_of_dwarf:
        member.eat_favourite_dish()
