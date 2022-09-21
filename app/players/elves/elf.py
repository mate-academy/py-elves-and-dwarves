from app.players.player import ABC, Player


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument
        self.nickname = nickname

    def play_elf_song(self) -> None:
        nick = self.nickname
        instrument = self._musical_instrument
        print(f"{nick} is playing a song on the {instrument}")
