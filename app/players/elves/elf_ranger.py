from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int
                 ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self.bow_level = bow_level

    @property
    def bow_level(self) -> int:
        return self._bow_level

    @bow_level.setter
    def bow_level(self, value: int) -> None:
        self._bow_level = value

    def get_rating(self) -> int:
        return self.bow_level * 3

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. {self.nickname} has bow "
            f"of the {self.bow_level} level"
        )
