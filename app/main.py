
def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(band: list) -> None:
    for elf in band:
        elf.play_elf_song()


def feast_of_the_dwarves(cohort: list) -> None:
    for dwarf in cohort:
        dwarf.eat_favourite_dish()
