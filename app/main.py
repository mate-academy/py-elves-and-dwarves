def calculate_team_total_rating(players: list) -> int:
    team_sum = 0
    for player in players:
        team_sum += player.get_rating()
    return team_sum


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
