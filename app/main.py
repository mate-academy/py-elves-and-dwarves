from .players.elves.elf_ranger import ElfRanger
from .players.elves.druid import Druid
from .players.dwarves.dwarf_warrior import DwarfWarrior
from .players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from .players.elves.elf import Elf
from .players.dwarves.dwarf import Dwarf
from .players.player import Player
from typing import List


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
