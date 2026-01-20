from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        return self._bow_level * 3

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} "
                f"has bow of the {self._bow_level} level")

    def play_music(self) -> str:
        print(
            f"{self.nickname} "
            f"is playing a song on the {self._musical_instrument} "
            f"while shooting arrows with a bow level of {self._bow_level}")
