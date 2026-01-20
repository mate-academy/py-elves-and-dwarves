from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player_of_team.get_rating() for player_of_team in team)


def elves_concert(choir_of_elves: list[Elf]) -> None:
    for elf in choir_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(team_of_dwarves: list[Dwarf]) -> None:
    for dwarv in team_of_dwarves:
        dwarv.eat_favourite_dish()
