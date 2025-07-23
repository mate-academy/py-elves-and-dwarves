from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players:list):
    return sum(player.get_rating() for player in players)

def elves_concert(elfs:list):
    for elf in elfs:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarfs:list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()