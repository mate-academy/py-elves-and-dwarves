def calculate_team_total_rating(team):
    return sum(member.get_rating() for member in team)


def elves_concert(list_of_elfs):
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs):
    for dwarf in list_of_dwarfs:
        dwarf.eat_favourite_dish()
