from app.players.player import Player
from app.players.elves.elf import Elf


class ElfRanger(Elf, Player):
    def __init__(self, bow_level: int,
                 nickname: str,
                 musical_instrument: str) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow of the " \
               f"{self._bow_level} level"

    def get_rating(self) -> int:
        return self._bow_level * 3
