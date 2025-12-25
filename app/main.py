from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> None:
    return sum(player.get_rating() for player in players)


def elves_concert(elf: list[Elf]) -> None:
    for human in elf:
        human.play_elf_song()


def feast_of_the_dwarves(dwarf: list[Dwarf]) -> None:
    for human in dwarf:
        human.eat_favourite_dish()
