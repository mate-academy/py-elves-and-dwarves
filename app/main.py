def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def calculate_team_total_rating(team: list) -> None:
    total = 0
    for player in team:
        one_player = player.get_rating()
        total += one_player
    return total


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
