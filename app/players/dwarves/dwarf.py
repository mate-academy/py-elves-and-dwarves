from app.players.player import Player

class Dwarf(Player):
    def __init__(self, nickname: str, power: int):
        super().__init__(nickname, "Dwarf", power)
