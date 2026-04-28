from players.player import Player
from players.eleves.elf import Elf
from players.eleves.druid import Druid
from players.eleves.elf_ranger import ElfRanger
from players.dwarves.dwarf import Dwarf
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from players.dwarves.dwarf_warrior import DwarfWarrior

def calculate_team_total_rating(players: list) -> int:
    total = 0
    for player in players:
        total += player.get_rating()
    return total

def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()


dwarves = [
    DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
    DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
]
feast_of_the_dwarves(dwarves)
# "Thiddeal is eating French Fries"
# "Dwarf is eating Caesar Salad"