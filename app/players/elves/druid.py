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

    def player_info(self) -> str:
        spell_info = f"has a favourite spell: {self._favourite_spell}"
        return f"Druid {self.nickname}. {self.nickname} {spell_info}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)
