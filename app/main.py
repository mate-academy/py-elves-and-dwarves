def calculate_team_total_rating(players: list) -> float:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarvs: list) -> None:
    for dwarf in dwarvs:
        dwarf.eat_favourite_dish()
