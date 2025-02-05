def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves_team: list) -> None:
    for player in elves_team:
        player.play_elf_song()


def feast_of_the_dwarves(dwarves_team: list) -> None:
    for player in dwarves_team:
        player.eat_favourite_dish()
