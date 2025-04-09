def calculate_team_total_rating(team: list) -> int:
    return sum(team_member.get_rating() for team_member in team)


def elves_concert(elves: list) -> None:
    for el in elves:
        el.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dw in dwarves:
        dw.eat_favourite_dish()
