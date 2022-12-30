from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_of_players: list[Player]) -> int:
    sum_of_the_ratings = 0
    for player in list_of_players:
        sum_of_the_ratings += player.get_rating()
    return sum_of_the_ratings


def elves_concert(list_of_elves: list[Elf]) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
