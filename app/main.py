from __future__ import annotations
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(
        player_list:
        list[Druid | ElfRanger | DwarfWarrior | DwarfBlacksmith]
) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(elf_list: list[Elf]) -> None:
    for player in elf_list:
        player.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for player in dwarf_list:
        player.eat_favourite_dish()
