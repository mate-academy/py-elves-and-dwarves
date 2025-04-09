from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(player_list: list[Player]) -> int:
    value = 0
    for player in player_list:
        value += player.get_rating()
    return value


def elves_concert(elfs_list: list[Elf]) -> None:
    for elf in elfs_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_list: list[Dwarf]) -> None:
    for dwarf in dwarfs_list:
        dwarf.eat_favourite_dish()
