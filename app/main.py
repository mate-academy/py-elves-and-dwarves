from __future__ import annotations
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(team_member.get_rating() for team_member in team)


def elves_concert(elves_choir: list[Elf]) -> None:
    for elf_singer in elves_choir:
        elf_singer.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
