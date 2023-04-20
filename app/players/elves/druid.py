from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, favourite_spell: str, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname, musical_instrument=musical_instrument)
        self.favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self.favourite_spell)

    def print_info(self) -> None:
        print(f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}")
