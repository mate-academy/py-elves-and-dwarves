from app.player.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        self.__bow_level = bow_level
        super().__init__(nickname, musical_instrument)

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} "
                f"has bow of the {self.__bow_level} level")

    def get_rating(self) -> int:
        return self.__bow_level * 3
