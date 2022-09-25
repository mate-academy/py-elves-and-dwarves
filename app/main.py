def calculate_team_total_rating(
        player_list: list) -> int:
    total_rating = 0
    for player_ in player_list:
        total_rating += player_.get_rating()
    return total_rating


def elves_concert(elf_list: list) -> None:
    for elf_ in elf_list:
        elf_.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for dwarf_ in dwarf_list:
        dwarf_.eat_favourite_dish()
