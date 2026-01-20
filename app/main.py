def calculate_team_total_rating(team: list) -> int:
    res = []

    for number in team:
        res.append(number.get_rating())
    return sum(res)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dvarf in dwarves:
        dvarf.eat_favourite_dish()
