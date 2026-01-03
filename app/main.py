def calculate_team_total_rating(players_list: list) -> int:
    total_rating = 0
    for player in players_list:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves_list: list) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
