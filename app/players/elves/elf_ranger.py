from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, bow_level: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. {self.nickname} has "
            f"bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level
