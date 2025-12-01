from elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            favourite_spell : str
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: {self._favourite_spell}"
        )
