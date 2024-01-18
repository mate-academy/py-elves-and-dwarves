from __future__ import annotations

from typing import Any


def calculate_team_total_rating(players_list: list) -> int:
    return sum([player.get_rating() for player in players_list])


def elves_concert(elves: list) -> Any:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> Any:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
