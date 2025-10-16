def calculate_team_total_rating(team_list: list) -> int:
    return sum(elf.get_rating() for elf in team_list)


def elves_concert(elves_list: list) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
