def calculate_team_total_rating(players: list) -> float:
    summ_rating = 0
    for player in players:
        summ_rating += player.get_rating()
    return summ_rating


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarwes: list) -> None:
    for dwarw in dwarwes:
        dwarw.eat_favourite_dish()
