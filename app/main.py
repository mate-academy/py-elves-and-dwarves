def calculate_team_total_rating(persons: list) -> int:
    return sum(person.get_rating() for person in persons)


def elves_concert(persons: list) -> list[str]:
    return [person.play_elf_song() for person in persons]


def feast_of_the_dwarves(persons: list) -> list[str]:
    return [person.eat_favourite_dish() for person in persons]
