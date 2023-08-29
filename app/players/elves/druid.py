from elf import Elf


class Druid(Elf):
    def __init__(self, name: str,
                 mucical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(name, mucical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        first_part = f"Druid {self.name}. {self.name} has a favourite"
        second_part = f" spell: {self.favourite_spell}"
        return first_part + second_part

    def get_rating(self) -> int:
        return len(self._favourite_spell)
