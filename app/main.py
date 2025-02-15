def calculate_team_total_rating(team: list) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(team: list) -> None:
    for player in team:
        player.play_elf_song()


def feast_of_the_dwarves(team: list) -> None:
    for player in team:
        player.eat_favourite_dish()
