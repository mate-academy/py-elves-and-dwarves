def calculate_team_total_rating(players: list) -> int:
    return sum([cls.get_rating() for cls in players])


def elves_concert(list_of_elf: list) -> str:
    for els in list_of_elf:
        els.play_elf_song()
    return "\n"


def feast_of_the_dwarves(dwarves: list) -> str:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
    return "\n"
