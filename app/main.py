def calculate_team_total_rating(team: list) -> int:
    team_rating = 0
    for player in team:
        team_rating += player.get_rating()
    return team_rating


def elves_concert(elfes: list) -> None:
    for elf in elfes:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
