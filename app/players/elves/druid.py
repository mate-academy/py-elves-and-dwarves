from app.players.elves.elf import Elf


class Druid(Elf):

    def __init__(
            self,
            favourite_spell: str,
            nickname: str,
            musical_instrument: str
    ) -> None:
        self._favourite_spell = favourite_spell
        super().__init__(nickname=nickname,
                         musical_instrument=musical_instrument)

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)
