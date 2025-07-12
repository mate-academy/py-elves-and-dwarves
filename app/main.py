def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for team_member in team:
        total_rating += team_member.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
