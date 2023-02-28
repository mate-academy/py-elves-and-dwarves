from __future__ import annotations
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list) -> int:
    return sum([hero.get_rating() for hero in players])


def elves_concert(elves: list[Elf]) -> None:
    for hero in elves:
        hero.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for hero in dwarves:
        hero.eat_favourite_dish()
