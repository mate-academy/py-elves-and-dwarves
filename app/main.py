from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: List[Player]) -> int:
    total_rating = sum(player.get_rating() for player in players)
    return total_rating


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Player]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
