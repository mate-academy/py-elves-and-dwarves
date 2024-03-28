from app.main import Elf


class Druid(Elf):
    def __init__(self, favourite_spell: str) -> None:
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. {self.nickname} has a"
                f" favourite spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)
