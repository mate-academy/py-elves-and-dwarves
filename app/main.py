from .players.player import Player
from .players.elves.elf import Elf
from .players.dwarves.dwarf import Dwarf

def calculate_team_total_rating(team: list[Player]) -> int:
    total = 0
    for i in team:
        total += i.get_rating()
    return total


def elves_concert(elves: list[Elf]) -> None:
    for i in elves:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for i in dwarves:
        i.eat_favourite_dish()
