def calculate_team_total_rating(players_list):
    return sum([player.get_rating()for player in players_list])


def elves_concert(elfs_list):
    for elf in elfs_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list):
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
