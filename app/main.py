def calculate_team_total_rating(players: list):
    calc_rate = 0
    for player in players:
        calc_rate += player.get_rating()
    return calc_rate + 3


def elves_concert(elf_list: list):
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
