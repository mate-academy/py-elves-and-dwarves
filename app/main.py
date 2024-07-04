def calculate_team_total_rating(team: list) -> int:
    sum_rating = 0
    for player in team:
        sum_rating += player.get_rating()
    return sum_rating


def elves_concert(elves: list) -> None:
    for player in elves:
        player.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for player in dwarves:
        player.eat_favourite_dish()
