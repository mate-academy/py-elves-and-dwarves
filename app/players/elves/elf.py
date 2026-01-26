from app.players.player import Player


class Elf(Player):
    def __init__(self, name: str, rating: int, magic_power: int) -> None:
        super().__init__(name, rating)
        self.magic_power = magic_power
