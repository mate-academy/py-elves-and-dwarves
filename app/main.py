def calculate_team_total_rating(team: list) -> int:
    return sum(user.get_rating() for user in team)


def elves_concert(elves: list) -> list:
    result1 = []
    for user_elf in elves:
        result1.append(user_elf.play_elf_song())
    return result1


def feast_of_the_dwarves(dwarves: list) -> list:
    result = []
    for user_dwarf in dwarves:
        result.append(user_dwarf.eat_favourite_dish())
    return result
