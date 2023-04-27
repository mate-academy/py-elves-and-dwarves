from app.players.player import Player
from elf_ranger import ElfRanger
from druid import Druid



class Elf(Player):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song"
              f" on the {self._musical_instrument}")

    def get_rating(self):
        if isinstance(self, Elf):
            if isinstance(self, ElfRanger):
                return self._bow_level * 3
            else:
                return len(self._favourite_spell)

    def player_info(self):
        if isinstance(self, Elf):
            if isinstance(self, ElfRanger):
                return (f"Elf ranger {self.nickname}. {self.nickname} has bow "
                        f"of the {self._bow_level} level")
            else:
                return (f"Druid {self.nickname}. {self.nickname} has a "
                        f"favourite spell: {self._favourite_spell}")