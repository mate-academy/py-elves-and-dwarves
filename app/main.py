def calculate_team_total_rating(elves: list):
    team_power = 0
    for elf in elves:
        team_power += elf.get_rating()
    return team_power


def elves_concert(orchestra: list):
    for elf in orchestra:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
