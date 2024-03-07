class Druid(Elf):
    def __init__(self, favorite_spell: str, musical_instrument: str, nickname: str) -> None:
        super().__init__(musical_instrument, nickname)
        self._favorite_spell = favorite_spell

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favorite_spell}"

    def get_rating(self) -> int:
        return len(self._favorite_spell)