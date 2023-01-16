def calculate_team_total_rating(team: list) -> int:
    ratings = []
    for player in team:
        ratings.append(player.get_rating())
    return sum(ratings)


def elves_concert(elves_team: list) -> None:
    for player in elves_team:
        player.play_elf_song()


def feast_of_the_dwarves(dwarves_team: list) -> None:
    for player in dwarves_team:
        player.eat_favourite_dish()
