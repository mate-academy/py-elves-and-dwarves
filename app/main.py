from app.players.player import Player


def calculate_team_total_rating(team_members: list[Player]):
    return sum([member.get_rating() for member in team_members])
