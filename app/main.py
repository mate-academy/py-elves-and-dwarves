from typing import List

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(band: List[Elf]) -> None:
    for player in band:
        player.play_elf_song()


def feast_of_the_dwarves(dwarfs: List[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
