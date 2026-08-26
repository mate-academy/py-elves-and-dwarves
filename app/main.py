from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_of_teams: list[Player]) -> int:
    return sum(player.get_rating() for player in list_of_teams)


def elves_concert(list_of_elves: list[Elf]) -> None:
    for player in list_of_elves:
        player.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for player in dwarves:
        player.eat_favourite_dish()
