from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str
                 , musical_instrument: str, bow_level: str) -> None:
        self.nickname = nickname
        self._musical_instrument = musical_instrument
        self._bow_level = bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}.\
 {self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return self._bow_level * 3
