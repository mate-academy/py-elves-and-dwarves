from app.players.player import Player

from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team_list: list[Player]) -> int:
    return sum(member.get_rating() for member in team_list)


def elves_concert(team_list: list[Elf]) -> None:
    for member in team_list:
        member.play_elf_song()


def feast_of_the_dwarves(team_list: list[Dwarf]) -> None:
    for member in team_list:
        member.eat_favourite_dish()
