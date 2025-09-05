from app.players.elves.elf import Elf
from app.players.player import Player


class ElfRanger(Elf):
    _bow_level: int

    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int) -> None:
        Player.nickname = nickname
        Elf._musical_instrument = musical_instrument
        Elf._bow_level = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} "
                f"has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level
