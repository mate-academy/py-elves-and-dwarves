from typing import Any
from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list[Player]) -> int:
    total = sum(player.get_rating() for player in team)
    return total


def elves_concert(elves: list[Elf]) -> list[Any]:
    song = [elf.play_elf_song() for elf in elves]
    return song


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> list[Any]:
    return [dwarf.eat_favourite_dish() for dwarf in dwarves]
