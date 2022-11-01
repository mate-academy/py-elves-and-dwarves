def calculate_team_total_rating(team: list):
    return sum([raite.get_rating() for raite in team])


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
