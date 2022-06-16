def calculate_team_total_rating(list_of_players):
    total = 0
    for player in list_of_players:
        total += player.get_rating()
    return total


def elves_concert(list_of_elfs):
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves):
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
