def calculate_team_total_rating(players: list) -> int:
    result = 0

    for player in players:
        result += player.get_rating()
    return result


def elves_concert(players: list) -> None:
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: list) -> None:
    for player in players:
        player.eat_favourite_dish()
