from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(persons: list[Player]) -> int:
    return sum(person.get_rating() for person in persons)


def elves_concert(persons: list[Elf]) -> None:
    for person in persons:
        person.play_elf_song()


def feast_of_the_dwarves(persons: list[Dwarf]) -> None:
    for person in persons:
        person.eat_favourite_dish()
