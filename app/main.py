def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elf_list: list) -> None:
    for player in elf_list:
        player.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for player in dwarf_list:
        player.eat_favourite_dish()
