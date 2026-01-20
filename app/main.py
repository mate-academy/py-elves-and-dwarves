def calculate_team_total_rating(list_of_players: list) -> float:
    sum_rating = 0
    for item in list_of_players:
        sum_rating += item.get_rating()
    return sum_rating


def elves_concert(list_of_elfs: list) -> None:
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
