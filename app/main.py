def calculate_team_total_rating(payers: list):
    return sum([player.get_rating() for player in payers])


def elves_concert(elves: list):
    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list):
    [dwarf.eat_favourite_dish() for dwarf in dwarves]
