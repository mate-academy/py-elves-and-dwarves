from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(list_of_players: list[ElfRanger | Druid | DwarfWarrior | DwarfBlacksmith]) -> int:
    return sum([player.get_rating() for player in list_of_players])

def elves_concert(list_of_elves: list[Elf]):
    for elf in list_of_elves:
        elf.play_elf_song()

def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]):
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
