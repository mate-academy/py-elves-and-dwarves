from collections.abc import Iterable


def calculate_team_total_rating(team: Iterable) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: Iterable) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Iterable) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
