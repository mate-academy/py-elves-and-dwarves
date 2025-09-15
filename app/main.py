from typing import Any


def calculate_team_total_rating(players: Any) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elfs: Any) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Any) -> None:
    for dwarves in dwarves:
        dwarves.eat_favourite_dish()
