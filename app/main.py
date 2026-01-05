from app.players.player import Player

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(list_of_ratings: list[Player]) -> int:
    return sum(player.get_rating() for player in list_of_ratings)


def elves_concert(elfs_list: list[Elf]) -> None:
    for elf in elfs_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
