def calculate_team_total_rating(players: list) -> int:
    rating = 0
    for player in players:
        rating += player.get_rating()
    return rating


def elves_concert(bards: list) -> None:
    for singer in bards:
        singer.play_elf_song()


def feast_of_the_dwarves(dishes: list) -> None:
    for dish in dishes:
        dish.eat_favourite_dish()
