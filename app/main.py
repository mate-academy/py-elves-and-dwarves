def calculate_team_total_rating(players):
    return sum(player.get_rating() for player in players)


def elves_concert(elfves):
    for elf in elfves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
