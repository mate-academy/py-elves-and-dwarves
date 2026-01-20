from typing import List


def calculate_team_total_rating(players: List) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
