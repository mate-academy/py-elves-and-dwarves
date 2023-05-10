from app.players.player import Player


class Elf(Player):
    def __init__(self, musical_instrument: int) -> str:
        self._musical_instrument = musical_instrument

    def play_elf_song(self, nickname):
        print(f'{nickname} грає пісню на {self._musical_instrument}')
