def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for elf_play in elves:
        elf_play.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarves_feast in dwarves:
        dwarves_feast.eat_favourite_dish()
