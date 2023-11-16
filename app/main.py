from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(player_list: list[Player]) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(elves_list: list[Elf, ElfRanger, Druid]) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[
    Dwarf,
    DwarfWarrior,
    DwarfBlacksmith
]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
