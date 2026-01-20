from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int | float:
    return sum(member.get_rating() for member in team)


def elves_concert(team: list[Elf]) -> None:
    for member in team:
        member.play_elf_song()


def feast_of_the_dwarves(team: list[Dwarf]) -> None:
    for member in team:
        member.eat_favourite_dish()
