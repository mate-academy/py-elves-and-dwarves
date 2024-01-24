from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self.nickname = nickname
        self._musical_instrument = musical_instrument
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        name = self.nickname
        favourite_spell = self._favourite_spell
        return f"Druid {name}. {name} has a favourite spell: {favourite_spell}"
