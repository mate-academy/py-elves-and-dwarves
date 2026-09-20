from __future__ import annotations
















def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(players.get_rating())


def elves_concert(players: list[Elves]) -> None:
    for elf in players:
        elf.play_elf_song()


def feast_of_the_dwarves(players: list[Dwarves]) -> None:
    for dwarf in players:
        dwarf.eat_favourite_dish()
