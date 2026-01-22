from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(ls: list[Player]) -> int:
    return sum(char.get_rating() for char in ls)


def elves_concert(ls: list[Elf]) -> None:
    for char in ls:
        if isinstance(char, Elf):
            char.play_elf_song()


def feast_of_the_dwarves(ls: list[Dwarf]) -> None:
    for char in ls:
        if isinstance(char, Dwarf):
            char.eat_favourite_dish()
