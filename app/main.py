def calculate_team_total_rating(lista: list) -> int:
    points = 0
    for player in lista:
        points += player.get_rating()
    return points


def elves_concert(lista: list) -> None:
    for elf in lista:
        elf.play_elf_song()


def feast_of_the_dwarves(lista: list) -> None:
    for dwarf in lista:
        dwarf.eat_favourite_dish()
