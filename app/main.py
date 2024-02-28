from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Elf]) -> None:
    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        print(f"{dwarf.nickname} is eating {dwarf._favourite_dish}")
