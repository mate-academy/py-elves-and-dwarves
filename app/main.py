def calculate_team_total_rating(players: list) -> None:
    return sum(player.get_rating() for player in players)


def elves_concert(players: list) -> None:
    [player.play_elf_song() for player in players]


def feast_of_the_dwarves(players: list) -> None:
    [player.eat_favourite_dish() for player in players]
