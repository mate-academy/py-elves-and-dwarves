from app.players.player import Player


class Elf(Player):
    # Why don't the tests
    # throw errors if I haven't
    # specified the abstract methods get_rating and player_info?
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self.__musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song "
              f"on the {self.__musical_instrument}")
