from app.players import Player
class Dwarf(Player):

    def __init__(self, nickname, musical_instrument) -> None:
        super().__init__(nickname)
        self.musical_instrument = musical_instrument
