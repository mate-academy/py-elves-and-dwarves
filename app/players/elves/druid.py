from .elf import Elf


class Druid(Elf):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str,
    ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument,
        )
        self.favourite_spell = favourite_spell

    def get_rating(self) -> int:
        # rating = tamanho do favourite_spell
        return len(self.favourite_spell)

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: {self.favourite_spell}"
        )
