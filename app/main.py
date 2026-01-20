def calculate_team_total_rating(list_of_players: list) -> int:
    result = 0
    for player in list_of_players:
        result += player.get_rating()

    return result


def elves_concert(list_of_elfs: list):
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list):
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
