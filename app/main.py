from typing import List
from app.player.elves.elf import Elf
from app.player.players import Player
from app.player.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: List[Player]) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarve in dwarves:
        dwarve.eat_favourite_dish()
