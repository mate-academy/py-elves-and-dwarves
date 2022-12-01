def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elf_list: list) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_list: list) -> None:
    for dwarf in dwarfs_list:
        dwarf.eat_favourite_dish()
