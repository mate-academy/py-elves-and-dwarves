def calculate_team_total_rating(players: list) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()

    return total_rating


def elves_concert(elves: list) -> None:
    for _elf in elves:
        _elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for _dwarf in dwarves:
        _dwarf.eat_favourite_dish()
