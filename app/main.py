def calculate_team_total_rating(players: list):
    return sum(char.get_rating() for char in players)


def elves_concert(elves: list):
    [char.play_elf_song() for char in elves]


def feast_of_the_dwarves(dwarves: list):
    [char.eat_favourite_dish() for char in dwarves]
