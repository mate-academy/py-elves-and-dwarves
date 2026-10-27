from app.players.player import Player

from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior

from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elve in elves:
        elve.play_elf_song()


def feast_of_the_dwarves(dwarwes: list[Dwarf]) -> None:
    for dwarwe in dwarwes:
        dwarwe.eat_favourite_dish()


team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
print(calculate_team_total_rating(team))

elves = [
    Druid(
        nickname="Nardual",
        musical_instrument="flute",
        favourite_spell="aaa"
    ),
    ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33)
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
    )
]
feast_of_the_dwarves(dwarves)
