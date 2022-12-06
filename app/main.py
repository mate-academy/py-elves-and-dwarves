def calculate_team_total_rating(team: list) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(list_elves: list) -> list:
    return [elf.play_elf_song() for elf in list_elves]


def feast_of_the_dwarves(list_dwarves: list) -> list:
    return [dwarf.eat_favourite_dish() for dwarf in list_dwarves]
