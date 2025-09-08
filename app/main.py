from app.player.dwarves.dwarf import Dwarf
from app.player.elves.elf import Elf
from app.player.player import Player


def calculate_team_total_rating(team_list: list[Player]) -> int:
    return sum(player.get_rating() for player in team_list)


def elves_concert(team_list: list[Elf]) -> None:
    for player in team_list:
        if isinstance(player, Elf):
            player.play_elf_song()


def feast_of_the_dwarves(team_list: list[Dwarf]) -> None:
    for player in team_list:
        if isinstance(player, Dwarf):
            player.eat_favourite_dish()
