from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    total_rating = sum(player.get_rating() for player in team)
    return total_rating









