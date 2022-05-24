def calculate_team_total_rating(team: list):
    return sum(player.get_rating() for player in team)


def elves_concert(elf_team: list):
    for player in elf_team:
        player.play_elf_song()


def feast_of_the_dwarves(dwarf_team: list):
    for player in dwarf_team:
        player.eat_favourite_dish()
