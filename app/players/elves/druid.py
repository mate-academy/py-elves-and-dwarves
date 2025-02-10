from app.players.elves import elf


class Druid(elf.Elf):
    def __init__(
            self,
            favourite_spell: str,
            musical_instrument: str,
            nickname: str
    ) -> None:
        super().__init__(musical_instrument, nickname)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)
