def calculate_team_total_rating(team: list):
    ratings = []
    for player in team:
        ratings.append(player.get_rating())
    return sum(ratings)


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
