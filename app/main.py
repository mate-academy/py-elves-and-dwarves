from __future__ import annotations

from app.players.player import Player

from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid

from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list[Player]) -> int:
    """Calculate and return the combined rating of all players in a list."""
    total_rating = 0

    for player in players:
        total_rating += player.get_rating()

    return total_rating


def elves_concert(elves: list[Elf | ElfRanger | Druid]) -> None:
    """Make every elf in the list play their musical instrument."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(
        dwarves: list[Dwarf | DwarfWarrior | DwarfBlacksmith]
) -> None:
    """Make every dwarf in the list eat their favourite dish."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
