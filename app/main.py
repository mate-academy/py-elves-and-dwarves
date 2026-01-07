from app.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player .values() for player  in team())

def elves_concert(elf: list) -> list:
    for elves in elf:
        elves.play_elf_song()

def feast_of_the_dwarves(dwarves: list) -> list:
    for dwarf in dwarves:
        dwarf.eat_favorite_dish()