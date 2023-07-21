from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(elem.get_rating() for elem in players)


def elves_concert(list_elfs: list[Elf]) -> None:
    for elem in list_elfs:
        elem.play_elf_song()


def feast_of_the_dwarves(list_dwarves: list[Dwarf]) -> None:
    for elem in list_dwarves:
        elem.eat_favourite_dish()


team = [
    Druid(nickname="Druid",
          musical_instrument="flute",
          favourite_spell="ABC"),
    ElfRanger(nickname="Ranger",
              musical_instrument="trumpet",
              bow_level=33),
]
calculate_team_total_rating(team)

dwarves = [
    DwarfWarrior(nickname="Thiddeal",
                 favourite_dish="French Fries",
                 hummer_level=3),
    DwarfBlacksmith("BlackSmith", "Salad", 4),
]
feast_of_the_dwarves(dwarves)
