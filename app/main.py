from __future__ import annotations
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(players_list: list[Player]) -> int:
    sum_rating = sum([player.get_rating() for player in players_list])
    return sum_rating


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
