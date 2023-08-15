from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(ls_of_player: list) -> int:
    return sum([rating.get_rating() for rating in ls_of_player])


def elves_concert(ls_of_elf: list[ElfRanger, Druid]) -> None:
    for elf in ls_of_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(ls_of_dwarf: list[Dwarf]) -> None:
    for dwarf in ls_of_dwarf:
        dwarf.eat_favourite_dish()
