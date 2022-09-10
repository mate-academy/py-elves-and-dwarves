def calculate_team_total_rating(team):
    all_ratings = []
    for player in team:
        all_ratings.append(player.get_rating())
    return sum(all_ratings)


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
