from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str,
    ) -> None:
        super(Druid, self).__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        first_part = f"Druid {self.nickname}. "
        second_part = f"{self.nickname} has a "
        third_part = f"favourite spell: {self._favourite_spell}"
        return first_part + second_part + third_part

    def get_rating(self) -> int:
        return len(self._favourite_spell)
