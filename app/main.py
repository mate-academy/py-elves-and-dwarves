def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for player in elves:
        player.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for player in dwarves:
        player.eat_favourite_dish()
