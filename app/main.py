def calculate_team_total_rating(teams: list) -> int:
    result = [sum(team.get_rating() for team in teams)]
    return result[0]


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
