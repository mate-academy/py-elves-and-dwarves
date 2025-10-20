from __future__ import annotations
from typing import Sequence
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: Sequence[Player]) -> int:
    """Return total rating of all players."""
    return sum(player.get_rating() for player in players)


def elves_concert(elves: Sequence[Elf]) -> None:
    """Each elf plays a song."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Sequence[Dwarf]) -> None:
    """Each dwarf eats favourite dish."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
