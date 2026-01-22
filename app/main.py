def calculate_team_total_rating(players):
    return sum([player.get_rating() for player in players])


def elves_concert(elves):
    return [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves):
    return [dwarf.eat_favourite_dish() for dwarf in dwarves]
