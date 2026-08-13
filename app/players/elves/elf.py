from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self.__musical_instrument = musical_instrument

    def get_rating(self) -> int:
        pass

    def player_info(self) -> None:
        pass

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self.__musical_instrument}")