from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 bow_level: int, musical_instrument: str = None) -> str:
        self.nickname = nickname
        self.bow_level = bow_level
        self.musical_instrument = musical_instrument

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. {self.nickname} " \
               f"has bow of the {self.bow_level} level"

    def get_rating(self) -> int:
        return 3 * self.bow_level

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.musical_instrument}")
