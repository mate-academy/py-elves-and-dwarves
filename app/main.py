def calculate_team_total_rating(Player):
    total_rating = 0
    for pers in Player:
        total_rating += pers.get_rating()
    return total_rating


def elves_concert(elf):
    for pers in elf:
        pers.play_elf_song()


def feast_of_the_dwarves(dwarf):
    for pers in dwarf:
        pers.eat_favourite_dish()
