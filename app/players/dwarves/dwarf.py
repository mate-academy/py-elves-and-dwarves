from app.players.player import Player


class Dwarf(Player):
    def __init__(self, name: str, rating: int, strength: int) -> None:
        super().__init__(name, rating)
        self.strength = strength
