def calculate_team_total_rating(team: list) -> int:
    calculate_total_rating = 0
    for yy in team:
        if type(yy).__name__ == "Druid":
            calculate_total_rating += len(yy.favourite_spell)
        elif type(yy).__name__ == "ElfRanger":
            calculate_total_rating += 3 * yy.bow_level
        elif type(yy).__name__ == "DwarfWarrior":
            calculate_total_rating += yy.hummer_level + 4
        elif type(yy).__name__ == "DwarfBlacksmith":
            calculate_total_rating += yy.skill_level
        elif yy == []:
            calculate_total_rating = 0
    return calculate_total_rating


def elves_concert(elves: list) -> int:
    for yy in elves:
        print(f"{yy.nickname} is playing a song on the "
              f"{yy.musical_instrument}")


def play_elf_song(elves: list) -> int:
    for yy in elves:
        print(f"{yy.nickname} is playing a song on the "
              f"{yy.musical_instrument}")


def feast_of_the_dwarves(dwarves: list) -> int:
    for yy in dwarves:
        print(f"{yy.nickname} is eating {yy.favourite_dish}")


def eat_favourite_dish(dwarves: list) -> int:
    for yy in dwarves:
        print(f"{yy.nickname} is eating {yy.favourite_dish}")
