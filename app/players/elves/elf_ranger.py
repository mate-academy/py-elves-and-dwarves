from app.players.elves.elf import Elf


class ElfRanger(Elf):

    def __init__(self, **kwargs) -> None:
        nickname = kwargs.get("nickname")
        musical_instrument = kwargs.get("musical_instrument")
        bow_level = kwargs.get("bow_level")
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        result = str(f"Elf ranger {self.nickname}. {self.nickname} has bow")
        result += str(f" of the {self._bow_level} level")
        return result

    def get_rating(self) -> int:
        return 3 * self._bow_level
