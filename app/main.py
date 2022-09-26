def calculate_team_total_rating(list_of_players: list):
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
