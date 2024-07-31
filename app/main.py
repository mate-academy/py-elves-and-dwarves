from typing import List

from app.players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Player]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Player]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
