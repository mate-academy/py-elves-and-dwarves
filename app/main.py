def calculate_team_total_rating(team: list) -> int:
    return sum(per.get_rating() for per in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarv in dwarves:
        dwarv.eat_favourite_dish()
