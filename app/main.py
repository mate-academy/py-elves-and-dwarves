from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list[Elf, Dwarf]) -> int:
    return sum(elem.get_rating() for elem in players)


def elves_concert(list_elfs: list[ElfRanger, Druid]) -> None:
    for elem in list_elfs:
        elem.play_elf_song()


def feast_of_the_dwarves(list_dwarves: list[DwarfWarrior,
                                            DwarfBlacksmith]) -> None:
    for elem in list_dwarves:
        elem.eat_favourite_dish()
