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

    def play_elf_song(self) -> str:
        print(f"{self.nickname} is playing a song on "
              f"the {self._musical_instrument}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")
