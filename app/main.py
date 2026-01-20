from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(class_list: list[Player]) -> float:
    return sum(player.get_rating() for player in class_list)


def elves_concert(class_list: list[Elf]) -> None:
    for elf in class_list:
        elf.play_elf_song()


def feast_of_the_dwarves(class_list: list[Dwarf]) -> None:
    for dwarf in class_list:
        dwarf.eat_favourite_dish()
