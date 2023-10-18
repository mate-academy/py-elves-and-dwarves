def calculate_team_total_rating(players: list) -> int:
    total = 0
    for player in players:
        total += player.get_rating()
    return total


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
