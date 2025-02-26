from app.players.elves.elf import Elf


class Druid(Elf):

    def __init__(self, **kwargs) -> None:
        nickname = kwargs.get("nickname")
        musical_instrument = kwargs.get("musical_instrument")
        favourite_spell = kwargs.get("favourite_spell")
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        result = str(f"Druid {self.nickname}. {self.nickname} has a favourite")
        result += str(f" spell: {self._favourite_spell}")
        return result

    def get_rating(self) -> int:
        return len(self._favourite_spell)
