from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(team_elves: List[Elf]) -> None:
    for elf in team_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(team_dwarves: List[Dwarf]) -> None:
    for dwarf in team_dwarves:
        dwarf.eat_favourite_dish()
