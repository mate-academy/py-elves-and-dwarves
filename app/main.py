def calculate_team_total_rating(team):
    return sum([gamer.get_rating() for gamer in team])


def elves_concert(elves):
    for song in elves:
        song.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for gnom in dwarves:
        gnom.eat_favourite_dish()
