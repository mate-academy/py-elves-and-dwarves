from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(
            self,
            nickname: str,
            favorite_dish: str
    ) -> None:
        super().__init__(nickname)
        self._favorite_dish = favorite_dish

    def eat_favorite_dish(self) -> None:
        print(
            f"{self.nickname}"
            f" is eating "
            f"{self._favorite_dish}"
        )

    def get_rating(self) -> None:
        pass

    def get_info(self) -> None:
        pass
