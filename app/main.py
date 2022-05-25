def calculate_team_total_rating(team):
    return sum([i.get_rating() for i in team])


def elves_concert(elves):
    for i in elves:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for i in dwarves:
        i.eat_favourite_dish()
