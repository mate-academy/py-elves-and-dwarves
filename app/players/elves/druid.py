from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell: str, nickname: str, musical_instrument: str) -> str:
        self._favourite_spell = favourite_spell
        self.nickname = nickname
        self.musical_instrument = musical_instrument

    def player_info(self, hummer_level):
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}"

    def get_rating(self):
        return self.favourite_spell