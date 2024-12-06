def calculate_team_total_rating(list_player: list) -> int:
    return sum(player.get_rating() for player in list_player)


def elves_concert(list_elf: list) -> None:
    for elf in list_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarf: list) -> None:
    for dwarf in list_dwarf:
        dwarf.eat_favourite_dish()
