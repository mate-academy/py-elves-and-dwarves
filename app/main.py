def calculate_team_total_rating(team: list) -> int:
    result = 0
    for member in team:
        result += member.get_rating()
    return result


def elves_concert(list_of_elves: list) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
