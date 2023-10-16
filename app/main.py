def calculate_team_total_rating(team: list) -> int:
    return sum(i.get_rating() for i in team)


def elves_concert(elf: list) -> None:
    for i in elf:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for i in dwarves:
        i.eat_favourite_dish()
