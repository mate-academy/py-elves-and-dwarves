from app.players.players import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self.__musical_instrument = musical_instrument
        super().__init__(nickname)

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song one the {self.__musical_instrument}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass
