# write your code here
from typing import List

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: List[Player]):
    total_rating = 0
    for member in team:
        total_rating += member.get_rating()
    return total_rating


def elves_concert(elves: List[Elf]):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
