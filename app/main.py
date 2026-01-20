from typing import List

from .players.dwarves.dwarf import Dwarf
from .players.elves.elf import Elf
from .players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    """Retorna a soma dos ratings do time."""
    return sum(member.get_rating() for member in team)


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
