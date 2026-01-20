from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from typing import List
from app.players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Druid]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[DwarfWarrior]) -> None:
    for dish in dwarves:
        dish.eat_favourite_dish()
