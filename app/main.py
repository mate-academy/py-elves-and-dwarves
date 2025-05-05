from players.dwarves.dwarf_warrior import DwarfWarrior
from players.elves.druid import Druid
from players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating() -> int:
    team = [
        Druid(nickname="Druid",
              musical_instrument="flute", favourite_spell="ABC"),
        ElfRanger(nickname="Ranger",
                  musical_instrument="trumpet", bow_level=33),
    ]

    return sum(player.get_rating() for player in team)


def elves_concert() -> None:
    elves = [
        Druid(nickname="Nardual",
              musical_instrument="flute", favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion",
                  musical_instrument="trumpet", bow_level=33),
    ]
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves() -> None:
    dwarves = [
        DwarfWarrior(nickname="Thiddeal",
                     favourite_dish="French Fries", hummer_level=3),
        DwarfWarrior(nickname="Dwarf",
                     favourite_dish="Caesar Salad", hummer_level=3),
    ]
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
