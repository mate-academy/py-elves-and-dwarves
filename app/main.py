def calculate_team_total_rating(teams: list):
    return sum(team.get_rating() for team in teams)


def elves_concert(elfs: tuple):
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
