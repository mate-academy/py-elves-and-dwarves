def calculate_team_total_rating(players: dict) -> int:
    total_rate = 0
    for hero in players:
        total_rate += hero.get_rating()
    return total_rate


def elves_concert(elves: list) -> None:
    for hero in elves:
        hero.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for hero in dwarves:
        hero.eat_favourite_dish()
