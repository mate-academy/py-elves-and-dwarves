from .players.player import Player
from .players.dwarves.dwarf import Dwarf
from .players.elves.elf import Elf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(person.get_rating() for person in team)


def elves_concert(team: list[Elf]) -> None:
    for elf in team:
        elf.play_elf_song()


def feast_of_the_dwarves(team: list[Dwarf]) -> None:
    for dwarf in team:
        dwarf.eat_favourite_dish()
