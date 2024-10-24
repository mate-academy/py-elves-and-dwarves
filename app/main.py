from typing import List

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: List[Player]) -> int:
    sum_rating = 0
    for player in players:
        sum_rating += player.get_rating()
    return sum_rating


def elves_concert(players: List[Player]) -> None:
    for player in players:
        if isinstance(player, Elf):
            player.play_elf_song()


def feast_of_the_dwarves(players: List[Player]) -> None:
    for player in players:
        if isinstance(player, Dwarf):
            player.eat_favourite_dish()
