def calculate_team_total_rating(players: list[Player]) -> int:
    suma = 0
    for player in players:
        suma += player.get_rating()
    return suma


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()



