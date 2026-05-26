# write your code here
from app.players.dwares.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(given_team: list[Player]) -> int:
    return sum(member.get_rating() for member in given_team)


def elves_concert(given_team: list[Elf]) -> None:
    for member in given_team:
        member.play_elf_song()


def feast_of_the_dwarves(given_team: list[Dwarf]) -> None:
    for member in given_team:
        member.eat_favourite_dish()
