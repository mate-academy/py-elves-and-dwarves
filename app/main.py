def calculate_team_total_rating(list_players: list) -> int:
    result = 0
    for i in list_players:
        result += i.get_rating()
    return result


def elves_concert(list_elves: list) -> None:
    for i in list_elves:
        i.play_elf_song()


def feast_of_the_dwarves(list_dwarves: list) -> None:
    for i in list_dwarves:
        i.eat_favourite_dish()
