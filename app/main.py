from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    sum_of_ratings = 0
    for player in players:
        sum_of_ratings += player.get_rating()

    return sum_of_ratings


def elves_concert(players_elves: list[Elf]) -> None:
    for elf in players_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(players_dwarves: list[Dwarf]) -> None:
    for dwarf in players_dwarves:
        dwarf.eat_favourite_dish()
