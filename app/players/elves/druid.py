from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self,
                 favourite_spell: str,
                 musical_instrument: str,
                 nickname: str
                 ) -> None:
        self.__favourite_spell = favourite_spell
        super().__init__(musical_instrument, nickname)

    def get_rating(self) -> int:
        return len(self.__favourite_spell)

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} " \
               f"has a favourite spell: {self.__favourite_spell}"
