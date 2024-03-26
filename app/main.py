from __future__ import annotations
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team_list: list[Player]) -> int:
    return sum([i.get_rating() for i in team_list])


def elves_concert(elves_list: list[Elf]) -> list:
    return [i.play_elf_song() for i in elves_list]


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> list:
    return [i.eat_favourite_dish() for i in dwarves_list]



