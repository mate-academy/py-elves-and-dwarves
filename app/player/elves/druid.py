from app.player.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        self.__favourite_spell = favourite_spell
        super().__init__(nickname, musical_instrument)

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. {self.nickname} "
                f"has a favourite spell: {self.__favourite_spell}")

    def get_rating(self) -> int:
        return len(self.__favourite_spell)
