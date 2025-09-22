from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 favourite_spell: str
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        calculate_rating = len(self._favourite_spell)
        return calculate_rating

    def player_info(self) -> str:
        info = (f"Druid {self.nickname}. {self.nickname} has a "
                f"favourite spell: {self._favourite_spell}")
        return info
