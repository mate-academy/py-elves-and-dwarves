from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell: str) -> str:
        self._favourite_spell = favourite_spell

    def player_info(self, nickname, hummer_level):
        return f"Druid {nickname}. {nickname} has a favourite spell: {self.favourite_spell}"

    def get_rating(self):
        return self.favourite_spell