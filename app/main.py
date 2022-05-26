def calculate_team_total_rating(team: list):
    return sum([player.get_rating() for player in team])


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf: list):
    for gnome in dwarf:
        gnome.eat_favourite_dish()
