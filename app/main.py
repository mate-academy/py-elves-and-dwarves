from app.players.player import Player


def calculate_team_total_rating(list_players: list | Player) -> int:
    total_rating = 0
    for player in list_players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(list_elfs: list) -> None:
    for elf in list_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarves: list) -> None:
    for dwarve in list_dwarves:
        dwarve.eat_favourite_dish()
