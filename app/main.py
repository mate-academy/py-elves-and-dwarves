from typing import List
from .players.elves.elf import Elf
from .players.dwarves.dwarf import Dwarf
from .players.elves.elf_ranger import ElfRanger
from .players.elves.druid import Druid
from .players.dwarves.dwarf_warrior import DwarfWarrior
from .players.player import Player


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
    print(ranger.get_rating())  # 21
    print(
        ranger.player_info()
    )  # Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level
    ranger.play_elf_song()  # Nardual Chaekian is playing a song on the flute

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )
    print(warrior.get_rating())  # 11
    print(
        warrior.player_info()
    )  # Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level
    warrior.eat_favourite_dish()  # Thiddeal is eating French Fries

    team = [
        Druid(
            nickname="Druid",
            musical_instrument="flute",
            favourite_spell="ABC"
        ),
        ElfRanger(
            nickname="Ranger",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]
    print(calculate_team_total_rating(team))  # 102

    elves = [
        Druid(
            nickname="Nardual",
            musical_instrument="flute",
            favourite_spell="aaa"
        ),
        ElfRanger(
            nickname="Rothilion",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior(
            nickname="Thiddeal",
            favourite_dish="French Fries",
            hummer_level=3
        ),
        DwarfWarrior(
            nickname="Dwarf",
            favourite_dish="Caesar Salad",
            hummer_level=3
        ),
    ]
    feast_of_the_dwarves(dwarves)
