from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname=nickname,
                         musical_instrument=musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        nick = self.nickname
        lvl = self._bow_level
        return f"Elf ranger {nick}. {nick} has bow of the {lvl} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level
