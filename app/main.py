from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: List[Player]) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(players: List[Elf]) -> None:
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: List[Dwarf]) -> None:
    for player in players:
        player.eat_favourite_dish()
