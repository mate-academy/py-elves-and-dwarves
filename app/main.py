def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list) -> str:
    return (elf.play_elf_song() for elf in elves)


def feast_of_the_dwarves(dwarves: list) -> str:
    return (dwarf.eat_favourite_dish() for dwarf in dwarves)
