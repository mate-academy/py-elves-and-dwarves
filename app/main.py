from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.player import Player
from typing import List


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List[ElfRanger]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[DwarfWarrior]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
