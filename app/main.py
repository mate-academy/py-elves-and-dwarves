def calculate_team_total_rating(ls_of_team: list) -> int:
    total_rating = 0
    for player in ls_of_team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(ls_of_elves: list) -> None:
    for elf in ls_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(ls_of_dwarfs: list) -> None:
    for dwarf in ls_of_dwarfs:
        dwarf.eat_favourite_dish()
