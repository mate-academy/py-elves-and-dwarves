

def calculate_team_total_rating(players_list: list) -> int:
    result = [player.get_rating() for player in players_list]
    return sum(result)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
