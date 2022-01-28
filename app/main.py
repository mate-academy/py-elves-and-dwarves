def calculate_team_total_rating(dream_team: list):
    return sum(mate.get_rating() for mate in dream_team)


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
