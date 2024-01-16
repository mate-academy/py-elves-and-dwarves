from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        elf_nick_str = f"Elf ranger {self.nickname}."
        elf_has_bow_str = f"{self.nickname} has bow"
        elf_bow_lvl_str = f"of the {self._bow_level} level"
        return f"{elf_nick_str} {elf_has_bow_str} {elf_bow_lvl_str}"

    def get_rating(self) -> str:
        return 3 * self._bow_level
