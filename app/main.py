from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(ls_of_player: list[Player]) -> int:
    return sum(rating.get_rating() for rating in ls_of_player)


def elves_concert(ls_of_elf: list[Elf]) -> None:
    for elf in ls_of_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(ls_of_dwarf: list[Dwarf]) -> None:
    for dwarf in ls_of_dwarf:
        dwarf.eat_favourite_dish()
