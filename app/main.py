def calculate_team_total_rating(
        player_list: list):
    total_rating = 0
    for player_ in player_list:
        total_rating += player_.get_rating()
    return total_rating


def elves_concert(elf_list: list):
    for elf_ in elf_list:
        elf_.play_elf_song()


def feast_of_the_dwarves(dwarv_list: list):
    for dwarv_ in dwarv_list:
        dwarv_.eat_favourite_dish()
