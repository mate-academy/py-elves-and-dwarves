from __future__ import annotations

from typing import Iterable

from app.players import Player, Elf, Dwarf


def calculate_team_total_rating(team: Iterable[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: Iterable[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Iterable[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
