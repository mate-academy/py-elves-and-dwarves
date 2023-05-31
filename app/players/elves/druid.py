from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
        self, nickname: str,
        musical_instrument: str,
        favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell: str = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. {self.nickname} has a "
                f"favourite spell: {self.favourite_spell}")

    def get_rating(self) -> int:
        return len(self.favourite_spell)

    @property
    def favourite_spell(self) -> str:
        return self._favourite_spell
