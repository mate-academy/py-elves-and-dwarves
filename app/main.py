def calculate_team_total_rating(players):
    rating = 0
    for player in players:
        rating += player.get_rating()
    return rating


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
