def calculate_team_total_rating(players_data: list) -> int:
    counter = 0
    for player in players_data:
        counter += player.get_rating()

    return counter


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
