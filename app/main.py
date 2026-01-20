
def calculate_team_total_rating(players: list) -> int:
    total = 0
    for char in players:
        total += char.get_rating()
    return total


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
