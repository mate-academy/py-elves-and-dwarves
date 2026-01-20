from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(lst: list[Player]) -> int:
    total = sum(player.get_rating() for player in lst)

    return total


def elves_concert(lst: list[Elf]) -> None:
    for elf in lst:
        elf.play_elf_song()


def feast_of_the_dwarves(lst: list[Dwarf]) -> None:
    for dwarf in lst:
        dwarf.eat_favourite_dish()
