from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        self._nickname = nickname
        self._musical_instrument = musical_instrument
        self._favourite_spell = favourite_spell

    def play_elf_song(self) -> None:
        print(f"{self._nickname} is playing a song on the "
              f"{self._musical_instrument}")

    def player_info(self) -> str:
        return (f"Druid {self._nickname}. {self._nickname} "
                f"has a favourite spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)
