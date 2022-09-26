def calculate_team_total_rating(players: list):
    sum_of_rating = 0
    for player in players:
        sum_of_rating += player.get_rating()
    return sum_of_rating


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
