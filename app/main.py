def calculate_team_total_rating(team):
    return sum(hero.get_rating() for hero in team)


def elves_concert(elves):
    for elve in elves:
        elve.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarve in dwarves:
        dwarve.eat_favourite_dish()
