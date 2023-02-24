from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    rating = 0
    for player in players:
        rating += player.get_rating()
    return rating


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for elf in dwarves:
        elf.eat_favourite_dish()
