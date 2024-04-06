from typing import List

from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(player_list: List[Player]) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(elven_list: List[Elf]) -> None:
    for elven in elven_list:
        elven.play_elf_song()


def feast_of_the_dwarves(dwarf_list: List[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
