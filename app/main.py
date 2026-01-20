def calculate_team_total_rating(persons: list) -> int:
    sum_of_ratings = 0
    for person in persons:
        sum_of_ratings += person.get_rating()
    return sum_of_ratings


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
