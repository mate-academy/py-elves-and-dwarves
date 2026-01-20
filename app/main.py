def calculate_team_total_rating(team: list) -> int:
    return sum(member.get_rating() for member in team)


def elves_concert(elves_list: list) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
