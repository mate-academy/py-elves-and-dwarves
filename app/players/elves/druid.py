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

    def player_info(self) -> None:
        return "Druid {0}. {0} has a favourite spell: {1}".format(
            self.nickname,
            self._favourite_spell
        )

    def get_rating(self) -> None:
        return len(self._favourite_spell)
