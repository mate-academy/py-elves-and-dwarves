def calculate_team_total_rating(lists: list) -> int:
    return sum(player.get_rating() for player in lists)


def elves_concert(lists: list) -> None:
    for player in lists:
        player.play_elf_song()


def feast_of_the_dwarves(lists: list) -> None:
    for player in lists:
        player.eat_favourite_dish()
