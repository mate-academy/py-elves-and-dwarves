def calculate_team_total_rating(team: list) -> int:
    return sum(elem.get_rating() for elem in team)


def elves_concert(elves: list) -> None:
    for elem in elves:
        elem.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarve in dwarves:
        dwarve.eat_favourite_dish()
