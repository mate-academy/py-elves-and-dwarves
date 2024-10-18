from typing import List

from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: List[Player]) -> int:
    """Calculate and return total team rating."""
    return sum([p.get_rating() for p in players])


def elves_concert(elfs: List[Elf]) -> None:
    """Make list of elves play instruments."""
    for elf in elfs:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: List[Dwarf]) -> None:
    """Make all dwarves in list eat."""
    for dwarf in dwarfs:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
