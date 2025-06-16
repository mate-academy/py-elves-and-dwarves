from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.player import Player
from typing import List


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[ElfRanger]) -> None:  # Використовуємо ElfRanger як приклад
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[DwarfWarrior]) -> None:  # Використовуємо DwarfWarrior як приклад
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
