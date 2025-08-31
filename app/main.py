from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf

from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith



def calculate_team_total_rating(names: list) -> int:
    result = []
    for i in names :
        result += i.get_rating()

def elves_concert(names: list) -> None:
    for i in names :
        i.play_elf_song()

def feast_of_the_dwarves(names: list) -> None:
    for i in names :
        i.eat_favourite_dish()
