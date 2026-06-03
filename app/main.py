from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(list_gamers: list[Player]) -> int:
    count_rating = 0

    for player in list_gamers:
        count_rating += player.get_rating()

    return count_rating


def elves_concert(list_elf: list[Elf]) -> None:
    for elf in list_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
