from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname=nickname,
                         musical_instrument=musical_instrument)
        self._favorite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favorite_spell)

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname}. {self.nickname} "
            f"has a favourite spell: {self._favorite_spell}"
        )
