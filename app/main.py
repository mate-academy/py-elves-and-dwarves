def calculate_team_total_rating(team: list) -> int:
    return sum(player_of_team.get_rating() for player_of_team in team)


def elves_concert(team: list) -> None:
    for elf in team:
        elf.play_elf_song()


def feast_of_the_dwarves(team: list) -> None:
    for dwarv in team:
        dwarv.eat_favourite_dish()
