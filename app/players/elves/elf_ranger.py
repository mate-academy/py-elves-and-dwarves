from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self, nickname: str, musical_instrument: str, bow_level: int
    ) -> None:
        super().__init__(musical_instrument)
        self.nickname = nickname
        self.__bow_level = bow_level

    def get_rating(self) -> int:
        return self.__bow_level * 3

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self.__bow_level} level"
        )
