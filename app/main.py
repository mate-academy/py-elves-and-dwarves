def calculate_team_total_rating(list_of_players: list) -> int:
    result = 0
    for player in list_of_players:
        result += player.get_rating()
    return result


def elves_concert(list_of_elf: list) -> None:
    for elf in list_of_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list) -> None:
    for dwarv in list_of_dwarves:
        dwarv.eat_favourite_dish()
