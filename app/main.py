from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


# Make these classes available when importing from main
__all__ = [
    "ElfRanger",
    "Druid",
    "DwarfWarrior",
    "DwarfBlacksmith",
    "calculate_team_total_rating",
    "elves_concert",
    "feast_of_the_dwarves",
]
