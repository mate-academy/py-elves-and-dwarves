def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for person in team:
        total_rating += person.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for draw in dwarves:
        draw.eat_favourite_dish()
