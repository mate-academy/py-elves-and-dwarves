from .elf import Elf


class Druid(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        info = "Druid {0}. {1} has a favourite spell: {2}"
        return info.format(self.nickname, self.nickname, self._favourite_spell)

    def get_rating(self) -> int:
        return len(self._favourite_spell)
