from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell) * 5

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname} plays {self._musical_instrument} "
            f"and casts {self._favourite_spell}"
        )
