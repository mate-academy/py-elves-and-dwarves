def calculate_team_total_rating(players: list):
    sum_rating = 0
    for player in players:
        sum_rating += player.get_rating()
    return sum_rating


def elves_concert(elfs: list):
    for el in elfs:
        el.play_elf_song()


def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
