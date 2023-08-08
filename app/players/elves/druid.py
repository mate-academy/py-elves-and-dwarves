from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        nk = self.nickname
        fs = self._favourite_spell
        return f"Druid {nk}. {nk} has a favourite spell: {fs}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)
