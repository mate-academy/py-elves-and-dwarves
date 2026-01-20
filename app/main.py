def calculate_team_total_rating(team: list) -> int:
    sums = 0
    for method in team:
        sums += method.get_rating()
    return sums


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
