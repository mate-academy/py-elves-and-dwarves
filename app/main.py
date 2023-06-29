from __future__ import annotations

from app.players.dwarves import Dwarf
from app.players.elves import Elf
from app.players import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    """Returns the sum of the ratings for all team members"""
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
