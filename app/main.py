from players.player import Player
from players.dwarves.dwarf import Dwarf
from players.elves.elf import Elf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([elem.get_rating() for elem in players])

def elves_concert(elfs: list[Elf]) -> None:
    for elem in elfs:
        elem.play_elf_song()

def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for elem in dwarves:
        elem.eat_favourite_dish()
