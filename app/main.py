def calculate_team_total_rating(list_of_players: list) -> int:
    return sum(players.get_rating() for players in list_of_players)


def elves_concert(list_of_elf: list) -> None:
    for elf in list_of_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_the_dwarves: list) -> None:
    for dwarves in list_of_the_dwarves:
        dwarves.eat_favourite_dish()
