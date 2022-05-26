def calculate_team_total_rating(players):
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
