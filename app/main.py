def calculate_team_total_rating(player_list: list) -> int:
    return sum([player.get_rating() for player in player_list])


def elves_concert(player_list: list) -> None:
    for player in player_list:
        player.play_elf_song()


def feast_of_the_dwarves(player_list: list) -> None:
    for player in player_list:
        player.eat_favourite_dish()
