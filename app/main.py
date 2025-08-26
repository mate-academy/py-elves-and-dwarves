from app.players.player import Player
#  from app.players.elves.druid import Druid
from app.players.elves.elf import Elf
#  from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf import Dwarf
#  from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
#  from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players_list: list[Player]) -> int | float:
    result = 0
    for person in players_list:
        result += person.get_rating()
    return result


def elves_concert(list_of_elves: list[Elf]) -> None:
    for person in list_of_elves:
        person.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for person in list_of_dwarves:
        person.eat_favourite_dish()
