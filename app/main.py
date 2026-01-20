def calculate_team_total_rating(team: list):
    return sum([player.get_rating() for player in team])


def elves_concert(elves: list):
    return [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list):
    return [dwarf.eat_favourite_dish() for dwarf in dwarves]
