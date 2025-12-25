from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self, nickname: str, musical_instrument: str, favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (f"Druid {self.nickname}."
                f" {self.nickname} has "
                f"a favourite spell: {self._favourite_spell}")

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing "
              f"a song on the {self._musical_instrument}")
