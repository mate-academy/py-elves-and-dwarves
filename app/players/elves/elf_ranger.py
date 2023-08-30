from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 name: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(name, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        first_part = f"Elf ranger {self.name}."
        second_part = f" {self.name} has bow of the"
        third_part = f" {self.bow_level} level"
        return first_part + second_part + third_part

    def get_rating(self) -> int:
        return 3 * self._bow_level
