def calculate_team_total_rating(player_list: list) -> int:
    power = 0
    for player in player_list:
        power += player.get_rating()
    return power


def elves_concert(elves_list: list) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
