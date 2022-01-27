def calculate_team_total_rating(team: list):
    return sum([some_one.get_rating() for some_one in team])


def elves_concert(team: list):
    for some_elf in team:
        some_elf.play_elf_song()


def feast_of_the_dwarves(team: list):
    for some_dwarve in team:
        some_dwarve.eat_favourite_dish()
