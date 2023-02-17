from __future__ import annotations

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(rating: list[Player]) -> int:
    return sum(player.get_rating() for player in rating)


def elves_concert(elf_songs: list[Elf]) -> None:
    for song in elf_songs:
        song.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
