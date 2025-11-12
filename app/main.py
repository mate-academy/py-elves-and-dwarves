from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith

def calculate_team_total_rating(players: list[Player]) -> int:

    return sum(p.get_rating() for p in players)

def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()


