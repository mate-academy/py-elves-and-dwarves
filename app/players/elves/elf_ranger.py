from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, bow_level: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__bow_level = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} "
                f"has bow of the {self.__bow_level} level")

    def get_rating(self) -> int:
        return 3 * self.__bow_level
