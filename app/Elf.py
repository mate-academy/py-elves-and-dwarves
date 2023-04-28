from app.Player import Player


class Elf(Player):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str
    ) -> None:
        super().__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self._musical_instrument}")



class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self._bow_level = bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. {self.nickname} " \
               f"has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} " \
               f"has a favourite spell: {self._favourite_spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)
