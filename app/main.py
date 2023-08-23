from app.players.Player import Player


def calculate_team_total_rating(players: list) -> int:
    team_rating = 0
    for player in players:
        if isinstance(player, Player):
            player_rating = player.get_rating()
            team_rating += player_rating
    return team_rating


def elves_concert(elves: list) -> str:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> str:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
