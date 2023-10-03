
def calculate_team_total_rating(team) -> int:
    total_rating = sum(player.get_rating() for player in team)
    return total_rating


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
