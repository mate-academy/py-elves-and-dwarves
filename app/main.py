def calculate_team_total_rating(list_of_players: list) -> int:
    return sum([player.get_rating() for player in list_of_players])


def elves_concert(list_of_elfs: list) -> None:
    for i in range(len(list_of_elfs)):
        list_of_elfs[i].play_elf_song()


def feast_of_the_dwarves(list_of_dwarfes: list) -> None:
    for i in range(len(list_of_dwarfes)):
        list_of_dwarfes[i].eat_favourite_dish()
