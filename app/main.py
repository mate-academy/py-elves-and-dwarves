def calculate_team_total_rating(players: list = None):
    if players is None:
        players = []
    rat = 0

    for player in players:
        rat += player.get_rating()
    return  rat

def elves_concert(players: list = None):
    if players is None:
        players = []

    for player in players:
        player.play_elf_song()

def feast_of_the_dwarves(players: list = None):
    if players is None:
        players = []

    for player in players:
        player.eat_favourite_dish()
