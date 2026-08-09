

def calculate_team_total_rating(list_of_rating: list) -> int:
    total = 0
    for i in list_of_rating:
        total += i.get_rating()

    return total


def elves_concert(elf_list: list) -> str:
    for i in elf_list:
        i.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> str:
    for i in dwarves_list:
        i.eat_favourite_dish()
