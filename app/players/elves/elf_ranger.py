from abc import ABC
from app.players.elves.elf import Elf


class ElfRanger(Elf, ABC):
    def __init__(self, nickname: str, musical_instrument: str, bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self.bow_level = bow_level

    def get_rating(self) -> int | None:
        return self.bow_level * 3

    def player_info(self) -> None:
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self.bow_level} level")
