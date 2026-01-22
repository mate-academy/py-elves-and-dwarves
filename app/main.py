def calculate_team_total_rating(team):
    res = 0
    for rating in team:
        res += rating.get_rating()
    return res


def elves_concert(elves):
    for music in elves:
        music.play_elf_song()


def feast_of_the_dwarves(dwarf):
    for food in dwarf:
        food.eat_favourite_dish()
