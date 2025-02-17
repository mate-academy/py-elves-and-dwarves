def calculate_team_total_rating(players: list) -> [int, float]:
    return sum(player.get_rating() for player in players)


def elves_concert(lst_elf: list) -> None:
    for elf in lst_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(lst_dw: list) -> None:
    for dw in lst_dw:
        dw.eat_favourite_dish()
