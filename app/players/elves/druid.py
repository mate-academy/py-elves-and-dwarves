from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, _musical_instrument: str,
                 nickname: str, _favourite_spell: str) -> None:
        super().__init__(_musical_instrument, nickname)
        self._favourite_spell = _favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)
