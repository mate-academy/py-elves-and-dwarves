from players.player import Player
from players.elves.elf import Elves
from players.dwarves.dwarf import Dwarf


def calculate_team_total_rating() -> int:
    team = [Player()]
    return sum(team)


def elves_concert() -> None:
    elves = [Elves()]
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves() -> None:
    dwarves = [Dwarf()]
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
