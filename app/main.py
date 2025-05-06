def calculate_team_total_rating(team: list) -> int:
    team_ratings = []
    for team_player in team:
        team_ratings.append(team_player.get_rating())
    return sum(team_ratings)


def elves_concert(elves: list) -> str:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> str:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
