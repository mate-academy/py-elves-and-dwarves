from __future__ import annotations
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.player import Player


def calculate_team_total_rating(players_list: list[Player]) -> int | float:
    return sum(player.get_rating() for player in players_list)


def elves_concert(elves_list: list[Druid | ElfRanger]) -> None:
    if DwarfWarrior or DwarfBlacksmith not in elves_list:
        [elf.play_elf_song() for elf in elves_list]


def feast_of_the_dwarves(dwarves_list: list[DwarfWarrior
                                            | DwarfBlacksmith]) -> None:
    if ElfRanger or Druid not in dwarves_list:
        [dwarf.eat_favourite_dish() for dwarf
         in dwarves_list]
