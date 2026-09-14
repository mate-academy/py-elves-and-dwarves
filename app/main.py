from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: List[Player]) -> int:
    total = 0
    for player in team:
        total += player.get_rating()
    return total


def elves_concert(elves: List[Elf]) -> None:
    for player in elves:
        player.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for player in dwarves:
        player.eat_favourite_dish()
