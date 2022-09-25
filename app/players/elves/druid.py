from app.players.elves.elf import Elf
from app.players.player import Player


class Druid(Elf, Player):

    def __init__(self, nickname: str,
                 musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(musical_instrument, nickname)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return f"Druid {self.nickname}. " \
               f"{self.nickname} has a favourite spell: " \
               f"{self._favourite_spell}"
