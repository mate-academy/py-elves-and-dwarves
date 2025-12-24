

def calculate_team_total_rating(gamers: list) -> int:
    rating = 0
    for gamer in gamers:
        rating += gamer.get_rating()
    return rating


def elves_concert(singers: list) -> None:
    for singer in singers:
        singer.play_elf_song()


def feast_of_the_dwarves(eaters: list) -> None:
    for eater in eaters:
        eater.eat_favourite_dish()
