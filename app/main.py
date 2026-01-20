def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for one in elves:
        one.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for one in dwarves:
        one.eat_favourite_dish()
