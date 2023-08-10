from abc import ABC
from app.players.elves.elf import Elf


class Druid(Elf, ABC):
    def __init__(self, _favourite_spell: str,
                 _musical_instrument: str, nickname: str) -> None:
        super().__init__(_musical_instrument, nickname)
        self.favourite_spell = _favourite_spell

    def get_rating(self) -> int:
        return len(self.favourite_spell)

    def player_info(self) -> None:
        print(f"Druid {self.nickname}. "
              f"{self.nickname} has a favourite spell: {self.favourite_spell}")
