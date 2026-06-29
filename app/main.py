from typing import List
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players_list: List[Player]) -> int:
    result_sum = 0
    for player in players_list:
        result_sum += player.get_rating()
    return result_sum


def elves_concert(elfs_list: List[Elf]) -> None:
    for elf in elfs_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_list: List[Dwarf]) -> None:
    for dwarf in dwarfs_list:
        dwarf.eat_favourite_dish()
