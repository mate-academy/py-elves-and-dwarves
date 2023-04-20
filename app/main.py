from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(members: list[Player]) -> int:
    result = 0
    for member in members:
        result += member.get_rating()

    return result


def elves_concert(members: list[Elf]) -> None:
    for member in members:
        member.play_elf_song()


def feast_of_the_dwarves(members: list[Dwarf]) -> None:
    for member in members:
        member.eat_favourite_dish()
