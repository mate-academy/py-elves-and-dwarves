def calculate_team_total_rating(team: list):
    total = 0
    for player in team:
        total += player.get_rating()
    return total


def elves_concert(elfs: list):
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
