from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        self._musical_instrument = musical_instrument
        self._favourite_spell = favourite_spell
        super().__init__(nickname, musical_instrument)

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")

    def play_elf_song(self) -> None:
        print(f"{self.nickname} "
              f"is playing a song on the {self._musical_instrument}")
