def calculate_team_total_rating(players_ls: list):
    return sum([player.get_rating() for player in players_ls])


def elves_concert(elfs_ls: list):
    for elf in elfs_ls:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_ls: list):
    for dwarf in dwarves_ls:
        dwarf.eat_favourite_dish()
