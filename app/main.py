def calculate_team_total_rating(teams: list) -> int:
    return sum(player.get_rating() for player in teams)


def elves_concert(team_elf: list) -> None:
    for elf in team_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(team_dwarves: list) -> None:
    for dwarf in team_dwarves:
        dwarf.eat_favourite_dish()
