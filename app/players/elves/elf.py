from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self.__protected = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self.__protected}")

    def get_rating(self):
        pass

    def player_info(self):
        pass
