from app.players.player import Player
from abc import abstractmethod


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    @abstractmethod
    def player_info(self) -> str:
        pass

    @abstractmethod
    def get_rating(self) -> int:
        pass

    def play_elf_song(self) -> str:
        return (
            f"{self.nickname}"
            f" is playing a song on the {self._musical_instrument}"
        )
