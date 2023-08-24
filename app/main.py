from typing import List


def calculate_team_total_rating(players: List[int]) -> int:
    team_rating = []
    for player in players:
        team_rating.append(player.get_rating())
    return sum(team_rating)


def elves_concert(elves: List[str]) -> str:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[str]) -> str:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
