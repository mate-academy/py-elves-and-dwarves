def calculate_team_total_rating(list_of_players):
    return sum([player.get_rating() for player in list_of_players])


def elves_concert(list_of_elves):
    for player in list_of_elves:
        player.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs):
    for player in list_of_dwarfs:
        player.eat_favourite_dish()
