def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
