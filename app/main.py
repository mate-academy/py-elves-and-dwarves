from __future__ import annotations
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int | float:
    return sum(player.get_rating() for player in players)


def elves_concert(musicians: list[Elf]) -> None:
    for musician in musicians:
        musician.play_elf_song()


def feast_of_the_dwarves(eaters: list[Dwarf]) -> None:
    for eater in eaters:
        eater.eat_favourite_dish()
