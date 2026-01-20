from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    result = sum(player.get_rating() for player in players)
    return result


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
