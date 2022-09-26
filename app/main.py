def calculate_team_total_rating(players):
    sum_of_rating = 0
    for player in players:
        sum_of_rating += player.get_rating()
    return sum_of_rating


def elves_concert(elfs):
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfes):
    for dwarf in dwarfes:
        dwarf.eat_favourite_dish()
