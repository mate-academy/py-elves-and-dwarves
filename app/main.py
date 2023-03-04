from __future__ import annotations
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elf: list[Elf]) -> None:
    [person.play_elf_song() for person in elf]


def feast_of_the_dwarves(dwarf: list[Dwarf]) -> None:
    [person.eat_favourite_dish() for person in dwarf]
