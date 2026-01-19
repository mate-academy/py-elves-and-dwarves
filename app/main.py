from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list) -> int:
    rating = 0
    for i in team:
        rating += i.get_rating()
    return rating


def elves_concert(elves: list[Elf]) -> None:
    for i in elves:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for i in dwarves:
        i.eat_favourite_dish()
