from .players.player import Player
from .players.elves.elf import Elf
from .players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
