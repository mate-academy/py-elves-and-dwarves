def calculate_team_total_rating(players):
    result = 0
    for player in players:
        result += player.get_rating()
    return result


def elves_concert(elfs):
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
