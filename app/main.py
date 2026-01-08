def calculate_team_total_rating(player_list: list) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(elf_list: list) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
