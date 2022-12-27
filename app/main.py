def calculate_team_total_rating(team: list) -> int:
    total_sum = 0
    for player in team:
        total_sum += player.get_rating()
    return total_sum


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
