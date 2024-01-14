from app.players.player import Player

from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list[Player]) -> int:
    # sum_rating = 0
    # for player in players:
    #     player_ = player
    #     sum_rating += player_.get_rating()
    return sum(player.get_rating() for player in players)


def elves_concert(elves_list: list[Elf]) -> None:
    for elven in elves_list:
        player_ = elven
        player_.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        player_ = dwarf
        player_.eat_favourite_dish()
