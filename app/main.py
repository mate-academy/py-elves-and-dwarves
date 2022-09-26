def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for member in team:
        total_rating += member.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for Dwarf in dwarves:
        Dwarf.eat_favourite_dish()
