from app.players.player import Player

from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf import Dwarf

from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.elves.elf import Elf


def calculate_team_total_rating(list_of_players: list) -> int:
    total_rate = 0
    for item in list_of_players:
        total_rate += item.get_rating()
    return total_rate


def elves_concert(list_of_elfs: list) -> None:
    for item in list_of_elfs:
        item.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs: list) -> None:
    for item in list_of_dwarfs:
        item.eat_favourite_dish()
