def calculate_team_total_rating(list_players: list) -> int | float:
    return sum(player.get_rating() for player in list_players)


def elves_concert(list_elf: list) -> None:
    [elf.play_elf_song() for elf in list_elf]


def feast_of_the_dwarves(list_dwarf: list) -> None:
    [dwarf.eat_favourite_dish() for dwarf in list_dwarf]
