


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(team: list[Elf]) -> int:
    return sum(player.play_elf_song() for player in team)


def feast_of_the_dwarves(team: list[Dwarf]) -> int:
    return sum(player.eat_favourite_dish() for player in team)
