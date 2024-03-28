from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list[Player]) -> None:
    return sum(player.get_rating() for player in team)


def elves_concert(elfes: list[Elf]) -> None:
    for elv in elfes:
        elv.play_elf_song()


def feast_of_the_dwarves(drawfers: list[Dwarf]) -> None:
    for draw in drawfers:
        draw.eat_favourite_dish()
