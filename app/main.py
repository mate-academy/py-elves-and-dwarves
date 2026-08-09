

def calculate_team_total_rating(list_of_rating: list) -> int:
    return sum(player.get_rating() for player in list_of_rating)


def elves_concert(elf_list: list) -> None:
    for i in elf_list:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for i in dwarves_list:
        i.eat_favourite_dish()
