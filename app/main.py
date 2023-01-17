from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    ratings = [player.get_rating() for player in team]
    return sum(ratings)


def elves_concert(elves_team: list[Elf]) -> None:
    for player in elves_team:
        player.play_elf_song()


def feast_of_the_dwarves(dwarves_team: list[Dwarf]) -> None:
    for player in dwarves_team:
        player.eat_favourite_dish()
