from typing import List

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(lst: List[Player]) -> int:
    rating = 0
    for player in lst:
        rating += player.get_rating()
    return rating


def elves_concert(lst: List[Elf]) -> None:
    for elf in lst:
        elf.play_elf_song()


def feast_of_the_dwarves(lst: List[Dwarf]) -> None:
    for dwarf in lst:
        dwarf.eat_favourite_dish()
