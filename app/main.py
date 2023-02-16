from typing import List

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: List[Player]) -> float:
    return sum(player.get_rating() for player in players)


def elves_concert(elfs: List[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
