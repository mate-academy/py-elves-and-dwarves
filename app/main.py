from typing import List

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(
    players_list: List[Player],
) -> int:
    return sum(player.get_rating() for player in players_list)


def elves_concert(elves_list: List[Elf]) -> None:
    for single_elf in elves_list:
        single_elf.play_elf_song()


def feast_of_the_dwarves(
    dwarves_list: List[Dwarf],
) -> None:
    for single_dwarf in dwarves_list:
        single_dwarf.eat_favourite_dish()
