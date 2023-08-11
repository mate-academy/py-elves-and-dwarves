from abc import ABC
from app.elves.elf import Elf


class ElfRanger(Elf, ABC):
    def __init__(self, _bow_level: int,
                 _musical_instrument: str, nickname: str) -> None:
        super().__init__(_musical_instrument, nickname)
        self.bow_level = _bow_level

    def get_rating(self) -> int:
        return self.bow_level * 3

    def player_info(self) -> None:
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
              f"{self.bow_level} level")
