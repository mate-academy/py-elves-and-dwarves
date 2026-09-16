class ElfRanger(Elf):
    def __init__(self, bow_level: int) -> None:
        self._bow_level = bow_level

    def player_info(self) -> None:
        print(f"Elf ranger {self.nickname}. {self.nickname} \
            has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level
