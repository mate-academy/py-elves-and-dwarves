def calculate_team_total_rating(player_list: list) -> float:
    total_rating = 0
    for player in player_list:
        total_rating += player.get_rating()

    return total_rating


def elves_concert(player_list: list) -> None:
    for player in player_list:
        player.play_elf_song()


def feast_of_the_dwarves(player_list: list) -> None:
    for player in player_list:
        player.eat_favourite_dish()
