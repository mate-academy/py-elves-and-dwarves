from app.players.player import Players
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid


def calculate_team_total_rating(team):
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()

def elves_concert(elves):
    for elves in elves:
        elves.play_elf_song()

def feast_of_the_dwarves(dwarves):
    for dwarves in dwarves:
        dwarves.eat_favourite_dish()