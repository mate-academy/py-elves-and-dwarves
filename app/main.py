def calculate_team_total_rating(players_list: list) -> int:
    return sum(player.get_rating() for player in players_list)


def elves_concert(players_list: list) -> None:
    for player in players_list:
        player.play_elf_song()


def feast_of_the_dwarves(players_list: list) -> None:
    for player in players_list:
        player.eat_favourite_dish()
