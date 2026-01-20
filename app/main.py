from __future__ import annotations

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int | float:
    return sum(team_member.get_rating() for team_member in team)


def elves_concert(team: list[Elf]) -> list:
    return [team_member.play_elf_song() for team_member in team]


def feast_of_the_dwarves(team: list[Dwarf]) -> list:
    return [team_member.eat_favourite_dish() for team_member in team]
