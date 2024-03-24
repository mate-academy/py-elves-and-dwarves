from typing import List

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: List[Player]) -> int:
    return sum(player.get_rating() for player in players_list)


def elves_concert(elfs_list: List[Elf]) -> None:
    [elf.play_elf_song() for elf in elfs_list]


def feast_of_the_dwarves(dwarfs_list: List[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarfs_list]
