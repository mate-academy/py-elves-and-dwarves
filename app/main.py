from players.elves.elf import Elf
from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating

def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
