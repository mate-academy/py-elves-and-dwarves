def calculate_team_total_rating(list_of_players: list) -> int:
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(list_of_elfs: list) -> None:
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs: list) -> None:
    for dwarf in list_of_dwarfs:
        dwarf.eat_favourite_dish()
