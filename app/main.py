from app.players.player import Player
from app.players.elves.elf_ranger import Elf
from app.players.dwarves.dwarf_blacksmith import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(team: list[Elf]) -> None:
    for player in team:
        player.play_elf_song()


def feast_of_the_dwarves(team: list[Dwarf]) -> None:
    for player in team:
        player.eat_favourite_dish()
