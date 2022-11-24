from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    total = 0
    for character in team:
        total += character.get_rating()
    return total


def elves_concert(elves: list[Elf]) -> None:
    for character in elves:
        character.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for character in dwarves:
        character.eat_favourite_dish()
