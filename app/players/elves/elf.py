from abc import ABC, abstractmethod

from app.players.player import Player


class Elf(Player, ABC):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str
    ) -> None:
        super().__init__(nickname)
        self.musical_instrument = musical_instrument

    @abstractmethod
    def play_elf_song(self) -> None:
        pass
