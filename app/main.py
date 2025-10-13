def calculate_team_total_rating(players: list) -> int:
    return sum(rate.get_rating() for rate in players)


def elves_concert(elves: list) -> None:
    for sing in elves:
        sing.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
