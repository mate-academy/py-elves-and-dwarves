def calculate_team_total_rating(players: list):
    return sum(
        player.get_rating() for player in players
    )


def elves_concert(elvs: list):
    for elf in elvs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
