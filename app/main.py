def calculate_team_total_rating(instances: list) -> int:
    return sum(instance.get_rating() for instance in instances)


def elves_concert(instances: list) -> str:
    for instance in instances:
        instance.play_elf_song()


def feast_of_the_dwarves(instances: list) -> str:
    for instance in instances:
        instance.eat_favourite_dish()
