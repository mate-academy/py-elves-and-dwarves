def calculate_team_total_rating(team: list) -> int:
    rating = 0
    for player in team:
        if type(player.get_rating()) == int:
            rating += player.get_rating()
    return rating


def elves_concert(team_elfs: list) -> None:
    for elf in team_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(team_dwarves: list) -> None:
    for dwarf in team_dwarves:
        dwarf.eat_favourite_dish()
