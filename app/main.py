def calculate_team_total_rating(list_of_players: list) -> int:
    return sum(rating.get_rating() for rating in list_of_players)


def elves_concert(list_of_elfs: list) -> None:
    for elfs in list_of_elfs:
        elfs.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list) -> None:
    for dwarfs in list_of_dwarves:
        dwarfs.eat_favourite_dish()
