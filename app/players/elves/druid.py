from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 favourite_spell: str
                 ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self.favourite_spell = favourite_spell

    @property
    def favourite_spell(self) -> str:
        return self._favourite_spell

    @favourite_spell.setter
    def favourite_spell(self, value: str) -> None:
        self._favourite_spell = value

    def get_rating(self) -> int:
        return len(self.favourite_spell)

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} has " \
               f"a favourite spell: {self.favourite_spell}"
