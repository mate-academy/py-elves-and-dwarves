def calculate_team_total_rating(player_list: list):
    rating = 0
    for player in player_list:
        rating += player.get_rating()
        return rating


def elves_concert(elves_list: list):
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list):
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
