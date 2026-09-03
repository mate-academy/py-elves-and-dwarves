def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)
