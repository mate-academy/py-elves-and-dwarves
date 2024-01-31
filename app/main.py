from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(li: list[Player]) -> int:
    return sum(race.get_rating() for race in li)


def elves_concert(li: list[Elf]) -> None:
    for elf in li:
        elf.play_elf_song()


def feast_of_the_dwarves(li: list[Dwarf]) -> None:
    for dwarf in li:
        dwarf.eat_favourite_dish()
