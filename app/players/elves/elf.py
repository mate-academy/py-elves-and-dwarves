from app.players.player import Player

class Elf(Player):
    def __init__(self, nickname: str, power: int):
        super().__init__(nickname, "Elf", power)
