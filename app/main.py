def calculate_team_total_rating(players):
    sum = 0
    for player in players:
        sum += player.get_rating()


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
