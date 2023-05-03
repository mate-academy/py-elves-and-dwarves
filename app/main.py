from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(members: list[Player]) -> int:
    return sum(member.get_rating() for member in members)


def elves_concert(members: list[Elf]) -> None:
    for member in members:
        member.play_elf_song()


def feast_of_the_dwarves(members: list[Dwarf]) -> None:
    for member in members:
        member.eat_favourite_dish()
