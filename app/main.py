from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    rating = 0
    for member in team:
        rating += member.get_rating()
    return rating


def elves_concert(musicians: list[Elf]) -> None:
    for member in musicians:
        member.play_elf_song()


def feast_of_the_dwarves(eaters: list[Dwarf]) -> None:
    for each in eaters:
        each.eat_favourite_dish()
