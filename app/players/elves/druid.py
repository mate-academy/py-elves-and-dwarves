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

    def player_info(self) -> str:
        druid_nick_str = f"Druid {self.nickname}."
        druid_fav_spell_str = f"{self.nickname} has a favourite spell: "
        return (
            f"{druid_nick_str} {druid_fav_spell_str}{self._favourite_spell}"
        )

    def get_rating(self) -> int:
        return len(self._favourite_spell)
