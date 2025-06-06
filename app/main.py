from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int | float:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list[Elf]) -> None:
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
