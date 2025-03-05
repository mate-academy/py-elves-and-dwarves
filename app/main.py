def calculate_team_total_rating(ls: list) -> int:
    return sum(play.get_rating() for play in ls)


def elves_concert(ls: list) -> None:
    for play in ls:
        play.play_elf_song()


def feast_of_the_dwarves(ls: list) -> None:
    for play in ls:
        play.eat_favourite_dish()
