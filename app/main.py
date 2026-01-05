def calculate_team_total_rating(team: list) -> int:
    return sum(i.get_rating() for i in team)


def elves_concert(elves: list) -> None:
    for elve in elves:
        elve.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarv in dwarves:
        dwarv.eat_favourite_dish()
