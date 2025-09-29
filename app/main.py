def calculate_team_total_rating(team_players: list) -> int:
    result = []

    for team_player in team_players:
        result.append(team_player.get_rating())

    return sum(result)


def elves_concert(elves: list) -> None:
    for elve in elves:
        elve.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
