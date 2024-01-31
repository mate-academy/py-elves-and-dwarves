from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(list_player: list[Player]) -> int:
    return sum(race.get_rating() for race in list_player)


def elves_concert(list_elf: list[Elf]) -> None:
    for elf in list_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarf: list[Dwarf]) -> None:
    for dwarf in list_dwarf:
        dwarf.eat_favourite_dish()
