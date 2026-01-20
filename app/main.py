def calculate_team_total_rating(players: list) -> int:
    result = sum([player.get_rating() for player in players])
    return result


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
