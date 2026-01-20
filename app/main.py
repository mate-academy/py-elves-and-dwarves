def calculate_team_total_rating(team: list) -> int:
    result = 0
    for player in team:
        result += player.get_rating()
    return result


def elves_concert(team: list) -> None:
    for elf in team:
        elf.play_elf_song()


def feast_of_the_dwarves(team: list) -> None:
    for dwarf in team:
        dwarf.eat_favourite_dish()
