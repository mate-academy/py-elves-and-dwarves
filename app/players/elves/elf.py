from app.players.player import Player
from abc import abstractmethod


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")

        @abstractmethod
        def get_rating(self) -> None:
            pass

        @abstractmethod
        def player_info(self) -> None:
            pass
