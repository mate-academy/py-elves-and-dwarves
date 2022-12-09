from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list[Elf]) -> None:
    for player in elves:
        player.play_elf_song()


def feast_of_the_dwarves(dvarves: list[Dwarf]) -> None:
    for player in dvarves:
        player.eat_favourite_dish()
