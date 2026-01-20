from typing import List

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    total = 0
    for hero in team:
        total += hero.get_rating()
    return total


def elves_concert(elves: List[Elf]) -> None:
    for hero in elves:
        hero.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for hero in dwarves:
        hero.eat_favourite_dish()
