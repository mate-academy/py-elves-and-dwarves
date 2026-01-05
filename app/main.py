

def calculate_team_total_rating(team: list) -> int:
    total = 0
    for i in team:
        total += i.get_rating()
    return total


def elves_concert(elves: list) -> str:
    for i in elves:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> str:
    for i in dwarves:
        i.eat_favourite_dish()
