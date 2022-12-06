from typing import Any


def calculate_team_total_rating(team: list) -> int:
    sum_rating = 0
    for player in team:
        sum_rating += player.get_rating()
    return sum_rating


def elves_concert(list_elves: list) -> list[Any]:
    elves = []
    for elf in list_elves:
        elves.append(elf.play_elf_song())
    return elves


def feast_of_the_dwarves(list_dwarves: list) -> None:
    dwarves = []
    for dwarf in list_dwarves:
        dwarves.append(dwarf.eat_favourite_dish())
