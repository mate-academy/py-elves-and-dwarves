from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, bow_level: int, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname, musical_instrument=musical_instrument)
        self.bow_level = bow_level

    def get_rating(self) -> int:
        self.bow_level *= 3
        return self.bow_level

    def print_info(self) -> None:
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self.bow_level} level")
