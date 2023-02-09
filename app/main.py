from typing import List

from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    total = 0
    for member in team:
        total += member.get_rating()
    return total


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[DwarfWarrior]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
