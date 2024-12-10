from app.players.player import Player
from typing import List


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(rating.get_rating() for rating in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
