

def calculate_team_total_rating(team: list) -> int:
    total = 0
    for character in team:
        total += character.get_rating()
    return total


def elves_concert(elves: list) -> None:
    for character in elves:
        character.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for character in dwarves:
        character.eat_favourite_dish()
