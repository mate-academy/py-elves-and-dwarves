from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()


def elves_concert(elfes: list[Elf]) -> None:
    for elf in elfes:
        elf.play_elf_song()
