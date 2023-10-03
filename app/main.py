def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elve in elves:
        elve.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarve in dwarves:
        dwarve.eat_favourite_dish()
