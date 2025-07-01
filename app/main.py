from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team_list: list[Player]) -> int:
    return sum(i.get_rating() for i in team_list)


def elves_concert(team_list: list[Elf]) -> None:
    [member.play_elf_song() for member in team_list]


def feast_of_the_dwarves(team_list: list[Dwarf]) -> None:
    [i.eat_favourite_dish() for i in team_list]
