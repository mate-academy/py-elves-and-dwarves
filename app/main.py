from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team_list: list[Player]) -> int:
    total = 0
    for i in team_list:
        total += i.get_rating()
    return total


def elves_concert(team_list: list[Elf]) -> None:
    for i in team_list:
        i.play_elf_song()


def feast_of_the_dwarves(team_list: list[Dwarf]) -> None:
    for i in team_list:
        i.eat_favourite_dish()
