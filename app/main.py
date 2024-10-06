def calculate_team_total_rating(team_lst: list[object]) -> int:
    return sum(character.get_rating() for character in team_lst)


def elves_concert(elf_list: list[object]) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_lst: list[object]) -> None:
    for dwarf in dwarf_lst:
        dwarf.eat_favourite_dish()
