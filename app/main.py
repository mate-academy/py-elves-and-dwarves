def calculate_team_total_rating(lst_of_players: list) -> int:
    result = 0
    for player in lst_of_players:
        result += player.get_rating()
    return result


def elves_concert(lst_of_elves: list) -> None:
    for elf in lst_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(lst_of_dwarves: list) -> None:
    for dwarf in lst_of_dwarves:
        dwarf.eat_favourite_dish()
