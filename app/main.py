from typing import Any, List


def calculate_team_total_rating(team: List[Any]) -> int:
    return sum([member.get_rating() for member in team])


def elves_concert(elves: List[Any]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Any]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
