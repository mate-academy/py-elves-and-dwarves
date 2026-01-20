from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        bow_level: int
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self.bow_level = bow_level

    def get_rating(self) -> int:
        return self.bow_level * 3

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
                f"{self.bow_level} level")

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.musical_instrument}")
