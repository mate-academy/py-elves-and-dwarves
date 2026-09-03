from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(
        self, nickname: str, favourite_dish: str, hummer_power: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_power = hummer_power

    def get_rating(self) -> int:
        return self._hummer_power + 3

    def introduce(self) -> None:
        print(
            f"I'm {self.nickname} and I have "
            f"a hummer power of {self._hummer_power}"
        )
