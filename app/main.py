from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_of_teams: list[Player]) -> int:
    calc_total = 0
    for obj in list_of_teams:
        calc_total += obj.get_rating()
    return calc_total


def elves_concert(list_of_elfs: list[Elf]) -> None:
    for obj in list_of_elfs:
        obj.play_elf_song()


def feast_of_the_dwarves(list_of_dwarf: list[Dwarf]) -> None:
    for obj in list_of_dwarf:
        obj.eat_favourite_dish()
