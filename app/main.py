from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list) -> int:
    return sum([w.get_rating() for w in players])

def elves_concert(elves_: list) -> None:
    for elf in elves_:
        elf.play_elf_song()

def feast_of_the_dwarves( dwarves_: list) -> None:
    for dwar in dwarves_:
        dwar.eat_favourite_dish()
