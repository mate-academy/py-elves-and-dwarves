from .elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favorite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favorite_spell = favorite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}."
                f" {self.nickname}"
                f" has a favorite spell: {self._favorite_spell}")

    def get_rating(self) -> int:
        return len(self._favorite_spell)

