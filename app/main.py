from typing import Optional


def calculate_team_total_rating(players: Optional[list]) -> None:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: Optional[list]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Optional[list]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
