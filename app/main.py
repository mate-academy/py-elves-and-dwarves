from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elf: list[Elf]) -> None:
    for each in elf:
        each.play_elf_song()


def feast_of_the_dwarves(dwarf: list[Dwarf]) -> None:
    for each in dwarf:
        each.eat_favourite_dish()
