from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from typing import List


def calculate_team_total_rating(list_of_players: List[Player]) -> int:
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(list_of_elves: List[Elf]):
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: List[Dwarf]) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
