from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_of_teams: list[Player]) -> int:
    result = 0
    for element in list_of_teams:
        result += element.get_rating()
    return result


def elves_concert(list_of_elfs: list[Elf]) -> None:
    for element in list_of_elfs:
        element.play_elf_song()


def feast_of_the_dwarves(list_of_dwarf: list[Dwarf]) -> None:
    for element in list_of_dwarf:
        element.eat_favourite_dish()
