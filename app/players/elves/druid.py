from app.players.elves.elf import Elf
from app.players.player import Player


class Druid(Elf):
    _favourite_spell: str

    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str) -> None:
        Player.nickname = nickname
        Elf._musical_instrument = musical_instrument
        Elf._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. {self.nickname}"
                f" has a favourite spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        return 3 * len(self._favourite_spell)
