from abc import ABC
from ..player import Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        # 1 quebra de linha: o print já acrescenta '\n'
        print(
            f"{self.nickname} is playing a song on the "
            f"{self.musical_instrument}"
        )
