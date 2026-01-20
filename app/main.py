def calculate_team_total_rating(players):
    rating = 0
    for player in players:
        rating += player.get_rating()
    return rating


def elves_concert(players):
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players):
    for player in players:
        player.eat_favourite_dish()
