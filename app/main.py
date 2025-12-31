from typing import Iterable, List

from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.player import Player


def calculate_team_total_rating(team: Iterable[Player]) -> int:
    """
    Return the sum of ratings for all players in the provided team.
    """
    return sum(player.get_rating() for player in team)


def elves_concert(elves: Iterable[Elf]) -> None:
    """
    Ask every elf in the collection to play their song.
    """
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Iterable[Dwarf]) -> None:
    """
    Ask every dwarf in the collection to eat their favourite dish.
    """
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


__all__: List[str] = [
    "Player",
    "Elf",
    "ElfRanger",
    "Druid",
    "Dwarf",
    "DwarfWarrior",
    "DwarfBlacksmith",
    "calculate_team_total_rating",
    "elves_concert",
    "feast_of_the_dwarves",
]
