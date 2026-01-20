from app.players.player import Player
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(player: list[Player]) -> int:
    return sum(rating.get_rating() for rating in player)


def elves_concert(elfs: list[ElfRanger, Druid]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[DwarfWarrior, DwarfBlacksmith]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
