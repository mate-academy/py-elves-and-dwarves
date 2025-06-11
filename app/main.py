def calculate_team_total_rating(team: list) -> int:
    return sum(
        value.get_rating() for value in team
    )


def elves_concert(elves: list) -> None:
    for song in elves:
        song.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
