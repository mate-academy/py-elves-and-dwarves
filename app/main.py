from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    sum_of_rating = 0
    for player in players:
        sum_of_rating += player.get_rating()
    return sum_of_rating


def elves_concert(elves: list[Elf]) -> None:
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarve in dwarves:
        dwarve.eat_favourite_dish()
