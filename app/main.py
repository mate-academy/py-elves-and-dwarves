def calculate_team_total_rating(team: list) -> int:
    all_rating = []
    for i in team:
        all_rating.append(i.get_rating())
    return sum(all_rating)


def elves_concert(elves: list) -> None:
    for i in elves:
        i.play_elf_song()


def feast_of_the_dwarves(dwarwes: list) -> None:
    for i in dwarwes:
        i.eat_favourite_dish()
