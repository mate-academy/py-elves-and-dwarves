from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. {self.nickname} has "
                f"a favourite spell: {self.__favourite_spell}")

    def get_rating(self) -> int:
        return len(self.__favourite_spell)
