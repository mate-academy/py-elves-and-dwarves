from __future__ import annotations

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(players: list[Elf]) -> None:
    [player.play_elf_song() for player in players]


def feast_of_the_dwarves(players: list[Dwarf]) -> None:
    [player.eat_favourite_dish() for player in players]
