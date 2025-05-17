from app.players.elves.elf import Elf

class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str, favorite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self.favorite_spell = favorite_spell

    def player_info(self) -> None:
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favorite_spell}"

    def get_rating(self) -> str:
        return str(len(self.favorite_spell))