from __future__ import annotations
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(our_team: list) -> int:
    their_rating = 0
    for team in our_team:
        their_rating += team.get_rating()
    return their_rating


def elves_concert(our_elfs: list[Elf]) -> None:
    for elf in our_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(our_dwarves: list[Dwarf]) -> None:
    for dwarf in our_dwarves:
        dwarf.eat_favourite_dish()
