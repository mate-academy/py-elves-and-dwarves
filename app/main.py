from app.players.player import Player
from app.players.dwarves.dwarf_blacksmith import Dwarf
from app.players.elves.druid import Elf
from typing import List


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


# first method is correct

def elves_concert(elves: List[Elf]) -> None:
    [elv.play_elf_song() for elv in elves]


# second one too

def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarves]
