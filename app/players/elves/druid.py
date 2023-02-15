from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self,
                 favourite_spell: str,
                 musical_instrument: str,
                 nickname: str) -> None:
        super().__init__(musical_instrument, nickname)
        self.__favourite_spell = favourite_spell

    def player_info(self) -> str:
        string = (f"Druid {self.nickname}."
                  f" {self.nickname} has"
                  f" a favourite spell: {self.__favourite_spell}")
        return string

    def get_rating(self) -> int:
        return len(self.__favourite_spell)
