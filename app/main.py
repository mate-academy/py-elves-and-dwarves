from typing import List

from .players.elves.elf_ranger import ElfRanger
from .players.dwarves.dwarf_warrior import DwarfWarrior
from .players.player import Player
from .players.elves.elf import Elf
from .players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    print(ranger.get_rating())
    print(ranger.player_info())
    ranger.play_elf_song()

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )
    print(warrior.get_rating())
    print(warrior.player_info())
    warrior.eat_favourite_dish()
