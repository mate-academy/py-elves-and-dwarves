def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for item in elves:
        item.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for item in dwarves:
        item.eat_favourite_dish()
