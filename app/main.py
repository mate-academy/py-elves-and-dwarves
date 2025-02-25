from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: List[Player]) -> float | int:
    result = []
    for char in team:
        result.append(char.get_rating())
    return sum(result)


def elves_concert(elves: List[Elf]) -> None:
    for char in elves:
        char.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for char in dwarves:
        char.eat_favourite_dish()
