from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(person_list: list) -> int:
    return sum(name.get_rating() for name in person_list)


def elves_concert(elves_list: list[Elf]) -> None:
    for name in elves_list:
        name.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> None:
    for name in dwarves_list:
        name.eat_favourite_dish()
