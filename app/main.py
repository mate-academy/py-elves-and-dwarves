def calculate_team_total_rating(players: list) -> float:
    sum_of_rating = 0
    for player in players:
        sum_of_rating += player.get_rating()

    return sum_of_rating


def elves_concert(elves: list) -> float:
    pass


def feast_of_the_dwarves(dwarves: list) -> float:
    pass
