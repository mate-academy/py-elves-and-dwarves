from players.elves.elf import Elf


class ElfRanger(Elf):
    # `ElfRanger` should be a child of `Elf`.
    # Its `__init__` method should take one additional parameter:
    # `bow_level` - an integer that shows the quality of the bow.
    # The `__init__` method should store it in the protected attribute.
    def __init__(self, nickname: str,
                 musical_instrument: str, bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        # `get_rating` method should return:
        # * 3 * `bow_level` for `ElfRanger`
        return 3 * self._bow_level

    def player_info(self) -> str:
        # * `"Elf ranger {nickname}. {nickname}
        # has bow of the {bow_level} level"` for `ElfRanger` instances
        return (f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the {self._bow_level} level")
