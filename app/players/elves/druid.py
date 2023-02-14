from app.players.elves.elf import Elf


class Druid(Elf):

    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> None:
        return f"Druid {self.nickname}. {self.nickname} \
has a favourite spell: {self._favourite_spell}"

    def get_rating(self) -> None:
        return len(self._favourite_spell)

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a \
song on the {self._musical_instrument}"
        )
