def calculate_team_total_rating(teams: list) -> int:
    total_rating = 0
    for player in teams:
        total_rating += player.get_rating()

    return total_rating


def elves_concert(elf_list: list) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
