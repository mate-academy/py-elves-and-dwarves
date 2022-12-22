def calculate_team_total_rating(pleyers: list) -> int:
    result = 0
    for pleyer in pleyers:
        result += pleyer.get_rating()
    return result


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
