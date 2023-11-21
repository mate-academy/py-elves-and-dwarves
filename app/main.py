def calculate_team_total_rating(team: list) -> int:
    rating_sum = 0
    for player in team:
        rating_sum += player.get_rating()
    return rating_sum


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
