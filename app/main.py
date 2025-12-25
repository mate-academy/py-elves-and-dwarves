from typing import List

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(lst: List[Player]) -> int:
    return sum(list(map(lambda x: x.get_rating(), lst)))


def elves_concert(lst: List[Elf]) -> None:
    list(map(lambda x: x.play_elf_song(), lst))


def feast_of_the_dwarves(lst: List[Dwarf]) -> None:
    list(map(lambda x: x.eat_favourite_dish(), lst))
