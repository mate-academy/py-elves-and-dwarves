from typing import List, Optional

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(
        list_of_players: Optional[List[Player]]
) -> int:
    sum_of_rating = 0

    for player in list_of_players:
        sum_of_rating += player.get_rating()

    return sum_of_rating


def elves_concert(list_of_elves: Optional[List[Elf]]) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs: Optional[List[Dwarf]]) -> None:
    for dwarf in list_of_dwarfs:
        dwarf.eat_favourite_dish()
