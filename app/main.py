

def calculate_team_total_rating(team: list) -> int:
    temp = 0
    for i in team:
        temp += i.get_rating()
    return temp


def elves_concert(team: list) -> None:
    for i in team:
        i.play_elf_song()


def feast_of_the_dwarves(team: list) -> None:
    for i in team:
        i.eat_favourite_dish()
