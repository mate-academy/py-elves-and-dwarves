from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(person.get_rating() for person in team)


def elves_concert(team: list[Elf]) -> None:
    for person in team:
        person.play_elf_song()


def feast_of_the_dwarves(team: list[Dwarf]) -> None:
    for person in team:
        person.eat_favourite_dish()
