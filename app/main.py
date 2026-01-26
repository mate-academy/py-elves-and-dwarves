from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(team_list: list[Player]) -> int:
    total_rating = 0
    for member in team_list:
        total_rating += member.get_rating()
    return total_rating


def elves_concert(elf_list: list[Elf]) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":

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
    calculate_team_total_rating(team)

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

    (feast_of_the_dwarves
     (dwarves))
