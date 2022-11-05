from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str, favourite_spell: str) -> None:
        super().__init__(nickname)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return f"Druid {self.nickname}. \
               {self.nickname} has a favourite spell: {self.favourite_spell}"
