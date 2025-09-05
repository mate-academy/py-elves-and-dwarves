def calculate_team_total_rating(players) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves):
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarv in dwarves:
        dwarv.eat_favourite_dish()
