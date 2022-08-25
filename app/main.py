def calculate_team_total_rating(players: list):
    all_rating = 0
    for i in players:
        all_rating += i.get_rating()
    return all_rating


def elves_concert(elfi_concert: list):
    for elfi in elfi_concert:
        elfi.play_elf_song()


def feast_of_the_dwarves(dish_person: list):
    for person in dish_person:
        person.eat_favourite_dish()
