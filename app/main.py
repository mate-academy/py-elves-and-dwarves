def calculate_team_total_rating(team: list) -> int:
    return sum(obj.get_rating() for obj in team)


def elves_concert(elves_team: list) -> None:
    for obj in elves_team:
        obj.play_elf_song()


def feast_of_the_dwarves(dwarfs_team: list) -> None:
    for obj in dwarfs_team:
        obj.eat_favourite_dish()
