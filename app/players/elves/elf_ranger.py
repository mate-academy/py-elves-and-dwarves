from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def play_elf_song(self) -> None:
        instrument = self._musical_instrument
        print(f"{self.nickname} is playing a song on the {instrument}")

    def player_info(self) -> str:
        nick = self.nickname
        bow = self._bow_level
        return f"Elf ranger {nick}. {nick} has bow of the {bow} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
