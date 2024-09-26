from app.players.player import Player
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(team: list[Player]) -> int:
    rating_sum = 0
    for player in team:
        rating_sum += player.get_rating()
    return rating_sum


def elves_concert(elves: list[Druid, ElfRanger]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[DwarfBlacksmith, DwarfWarrior]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
