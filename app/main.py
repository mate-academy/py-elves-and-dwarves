# from players.elves.elf_ranger import ElfRanger
# from players.elves.druid import Druid
# from players.dwarves.dwarf_warrior import DwarfWarrior
# from players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from .players.player import Player
from .players.elves.elf import Elf
from .players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
