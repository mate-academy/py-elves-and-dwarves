from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str,
                 musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname=nickname,
                         musical_instrument=musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        nick = self.nickname
        spell = self._favourite_spell
        return f"Druid {nick}. {nick} has a favourite spell: {spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)
