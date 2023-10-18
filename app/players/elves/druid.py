from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            _musical_instrument: str,
            _favourite_spell: str
    ) -> None:
        super().__init__(nickname, _musical_instrument)
        self._favourite_spell = _favourite_spell

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} \has a favorite spell: {self._favourite_spell}"

    def get_rating(self) -> None:
        return len(self._favourite_spell)
