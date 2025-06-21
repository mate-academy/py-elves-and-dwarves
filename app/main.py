def calculate_team_total_rating(players_list: list) -> int:
    rating_sum = 0
    for one_player in players_list:
        rating = one_player.get_rating()
        rating_sum += rating
    return rating_sum


def elves_concert(elves_list: list) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
