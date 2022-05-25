from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 favourite_spell):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song"
              f" on the {self._musical_instrument}")

    def get_rating(self):
        return len(self._favourite_spell)

    def player_info(self):
        return f"Druid {self.nickname}. " \
            f"{self.nickname} has a favourite spell: {self._favourite_spell}"
