from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    total_rate = 0
    for player in team:
        total_rate += player.get_rating()
    return total_rate


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
