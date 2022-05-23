def calculate_team_total_rating(list_of_payers: list):
    return sum([player.get_rating() for player in list_of_payers])


def elves_concert(list_of_elves: list):
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs):
    for dwarf in list_of_dwarfs:
        dwarf.eat_favourite_dish()
