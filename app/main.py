from __future__ import annotations

from typing import Iterable, List

from players.elves.druid import Druid
from players.elves.elf_ranger import ElfRanger
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from players.dwarves.dwarf import Dwarf
from players.elves.elf import Elf
from players.player import Player


def calculate_team_total_rating(team: Iterable[Player]) -> int:
    """Return sum of get_rating() for all players in the team."""
    return sum(player.get_rating() for player in team)


def elves_concert(elves: Iterable[Elf]) -> None:
    """Call play_elf_song for each elf in the iterable."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Iterable[Dwarf]) -> None:
    """Call eat_favourite_dish for each dwarf in the iterable."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    # Examples / lightweight tests (asserts) to match the spec examples.
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7,
    )
    assert ranger.get_rating() == 21
    assert (
        ranger.player_info()
        == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
    )
    # prints: Nardual Chaekian is playing a song on the flute
    ranger.play_elf_song()

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7,
    )
    assert warrior.get_rating() == 11
    assert (
        warrior.player_info()
        == "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
    )
    # prints: Thiddeal is eating French Fries
    warrior.eat_favourite_dish()

    # calculate_team_total_rating example from prompt
    team = [
        Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
        ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
    ]
    assert calculate_team_total_rating(team) == 102  # 3*33 + 3

    # elves_concert example
    elves = [
        Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
    ]
    elves_concert(elves)

    # feast_of_the_dwarves example
    dwarves = [
        DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
        DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
    ]
    feast_of_the_dwarves(dwarves)

    print("All example assertions passed.")
