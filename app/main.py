def calculate_team_total_rating(team):
    res = 0
    for teammate in team:
        res += teammate.get_rating()
    return res


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
