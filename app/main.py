def calculate_team_total_rating(elves: list) -> int:
    return sum(elf.get_rating() for elf in elves)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()