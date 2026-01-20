from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    result = 0
    for player in team:
        total_rating = player.get_rating()
        result += total_rating
    return result


team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]


print(calculate_team_total_rating(team))


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


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
print(elves_concert(elves))


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


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
    DwarfBlacksmith(
        nickname="Oses",
        favourite_dish="pelmeni",
        skill_level=10
    )
]
print(feast_of_the_dwarves(dwarves))
