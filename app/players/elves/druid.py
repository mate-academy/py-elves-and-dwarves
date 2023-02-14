from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self, nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        druid = f"Druid {self.nickname}. "
        name = f"{self.nickname} has "
        spell = f"a favourite spell: {self._favourite_spell}"
        return druid + name + spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)
