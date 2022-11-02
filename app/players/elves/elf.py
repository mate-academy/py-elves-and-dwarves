from app.players import Player
class Elf(Player):

    def __init__(self, nickname, musical_instrument) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument
