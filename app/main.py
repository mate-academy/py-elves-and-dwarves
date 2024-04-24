from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(team: list) -> int:
    total = 0
    for player in team:
        total += player.get_rating()
    return total


team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
calculate_team_total_rating(team=team)


def elves_concert(elves: list) -> None:
    for func in elves:
        func.play_elf_song()


elves = [
    Druid(nickname="Nardual",
          musical_instrument="flute",
          favourite_spell="aaa"),
    ElfRanger(nickname="Rothilion",
              musical_instrument="trumpet",
              bow_level=33),
]
elves_concert(elves=elves)


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwar in dwarves:
        dwar.eat_favourite_dish()


dwarves = [
    DwarfWarrior(nickname="Thiddeal",
                 favourite_dish="French Fries",
                 hummer_level=3),
    DwarfWarrior(nickname="Dwarf",
                 favourite_dish="Caesar Salad",
                 hummer_level=3),
]
feast_of_the_dwarves(dwarves=dwarves)
