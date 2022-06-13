def calculate_team_total_rating(players: list):
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
