from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(each.get_rating() for each in team)


def elves_concert(elves: list[Elf]) -> None:
    for each in elves:
        each.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for each in dwarves:
        each.eat_favourite_dish()
