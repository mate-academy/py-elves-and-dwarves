from .players.player import Player
from .players.dwarves.dwarf import Dwarf
from .players.elves.elf import Elf


def calculate_team_total_rating(players: list[Player]) -> int | float:
    return sum(player.get_rating() for player in players)


def elves_concert(elves_list: list[Elf]) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
