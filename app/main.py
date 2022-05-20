from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players):
    sum_of_rating = 0
    for player in players:
        sum_of_rating += player.get_rating()
    return sum_of_rating


def elves_concert(elfs):
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfes):
    for dwarf in dwarfes:
        dwarf.eat_favourite_dish()


team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
print(calculate_team_total_rating(team))

elves = [
    Druid(nickname="Nardual",
          musical_instrument="flute",
          favourite_spell="aaa"
          ),
    ElfRanger(nickname="Rothilion",
              musical_instrument="trumpet",
              bow_level=33
              )
]
elves_concert(elves)

dwarves = [
    DwarfWarrior(nickname="Thiddeal",
                 favourite_dish="French Fries",
                 hummer_level=3
                 ),
    DwarfWarrior(nickname="Dwarf",
                 favourite_dish="Caesar Salad",
                 hummer_level=3
                 ),
    DwarfBlacksmith(nickname="Smith",
                    favourite_dish="Borsch",
                    skill_level=4)
]
feast_of_the_dwarves(dwarves)
