from app.players.player import Player
from typing import List


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(play_list: List[Player]) -> None:
    for elf in play_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: List[Player]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
