from app.elves.elf import Elf
from app.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> None:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elvess in elves:
        elvess.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarve in dwarves:
        dwarve.eat_favourite_dish()
