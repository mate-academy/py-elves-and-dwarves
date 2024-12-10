def calculate_team_total_rating(teams: list) -> int:
    rating = 0
    for player in teams:
        rating += player.get_rating()
    return rating


def elves_concert(teams: list) -> None:
    for player in teams:
        player.play_elf_song()


def feast_of_the_dwarves(teams: list) -> None:
    for player in teams:
        player.eat_favourite_dish()
