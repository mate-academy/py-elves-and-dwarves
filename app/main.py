def calculate_team_total_rating(team: list) -> float:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for elves in elves:
        elves.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarves in dwarves:
        dwarves.eat_favourite_dish()
