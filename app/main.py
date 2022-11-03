def calculate_team_total_rating(player_list: list) -> int:
    sum_rating = 0
    for character in player_list:
        sum_rating += character.get_rating()
    return sum_rating


def elves_concert(elf_list: list) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
