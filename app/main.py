def calculate_team_total_rating(players_list):
    result = 0
    for player in players_list:
        result += player.get_rating()
    return result


def elves_concert(elves_list):
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list):
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
