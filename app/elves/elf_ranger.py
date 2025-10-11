from app.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str, bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self.bow_level = bow_level

    def player_info(self) -> None:
        return (f"Elf ranger {self.nickname}. {self.nickname} has bow of the"
              f" {self.bow_level} level")

    def get_rating(self) -> int:
        return 3 * self.bow_level
