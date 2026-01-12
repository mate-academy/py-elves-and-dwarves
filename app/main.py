from players.elves.druid import Druid
from players.elves.elf_ranger import ElfRanger
from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_tem_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)

def elves_concert(elves: list) -> None:
    for elf in elves:
        Elf.play_elf_song(elf)

def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        Dwarf.eat_favourite_dish(dwarf)
