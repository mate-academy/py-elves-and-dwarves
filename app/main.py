from players.player import Player
from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(users_list: list[Player]) -> int:
    total_rating = 0
    for user in users_list:
        total_rating += user.get_rating()
    return total_rating


def elves_concert(elfs_list: list[Elf]) -> None:
    for elf in elfs_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
