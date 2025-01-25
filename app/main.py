from typing import List
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players: List[object]) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: List[ElfRanger]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[DwarfWarrior]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
