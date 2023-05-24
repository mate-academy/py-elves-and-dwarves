from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list["Player"]) -> int:
    sum_rating = 0
    for member in team:
        sum_rating += member.get_rating()
    return sum_rating


def elves_concert(band: list["Elf"]) -> None:
    for member in band:
        member.play_elf_song()


def feast_of_the_dwarves(group: list["Dwarf"]) -> None:
    for member in group:
        member.eat_favourite_dish()
