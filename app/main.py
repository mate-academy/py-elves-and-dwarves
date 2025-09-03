def calculate_team_total_rating(players: list) -> int:
    team_total_rating = 0
    for player in players:
        team_total_rating += player.get_rating()
    return team_total_rating


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
