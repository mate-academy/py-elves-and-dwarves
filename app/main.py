def calculate_team_total_rating(teams: list):
    return sum(team.get_rating() for team in teams)


def elves_concert(elves: tuple):
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
