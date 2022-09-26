def calculate_team_total_rating(team: list):
    result = 0
    for player in team:
        result += player.get_rating()
    return result


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
