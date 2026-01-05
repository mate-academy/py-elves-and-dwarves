

def calculate_team_total_rating(team: list) -> int:
    s = 0
    for i in team:
        s += i.get_rating()
    return s


def elves_concert(elves: list) -> str:
    for i in elves:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> str:
    for i in dwarves:
        i.eat_favourite_dish()
