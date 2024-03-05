from typing import List

from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elfs: List[Elf]) -> None:
    for player_elf in elfs:
        player_elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for player_dwarf in dwarves:
        player_dwarf.eat_favourite_dish()
