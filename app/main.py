def calculate_team_total_rating(group):
    sum_of_rate = 0
    for instance in group:
        sum_of_rate += instance.get_rating()
    return sum_of_rate


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
