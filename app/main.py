from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from typing import List

if __name__ == "__main__":
    elf_ranger = ElfRanger
    druid = Druid
    dwarf_warrior = DwarfWarrior
    dwarf_blacksmith = DwarfBlacksmith


def calculate_team_total_rating(players: list) -> int:
    total = 0
    for player in players:
        total += player.rating
    return total


def elves_concert(Elf: list, play_elf_song: list) -> None:
    for elf in Elf:
        elf.play_song(play_elf_song)


def feast_of_the_dwarves(Dwarf: list, eat_favourite_dish: list) -> None:
    for dwarf in Dwarf:
        dwarf.favourite_dish(eat_favourite_dish)
