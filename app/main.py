def calculate_team_total_rating(team: list):
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list):
    for el in elves:
        el.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dw in dwarves:
        dw.eat_favourite_dish()
