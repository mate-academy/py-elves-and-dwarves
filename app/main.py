def calculate_team_total_rating(players: list) -> int:
    res = 0
    for player in players:
        res += player.get_rating()

    return res


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
