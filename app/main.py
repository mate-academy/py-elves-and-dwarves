def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for player in elves:
        player.play_elf_song()


def feast_of_the_dwarves(dvarves: list) -> None:
    for player in dvarves:
        player.eat_favourite_dish()
