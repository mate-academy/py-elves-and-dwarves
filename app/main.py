def calculate_team_total_rating(team: list):
    rating = 0
    for player in team:
        rating += player.get_rating()
    return rating


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
