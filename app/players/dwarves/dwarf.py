from abc import ABC

from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname: str) -> None:
        super().__init__(nickname)

    def eat_favourite_dish(self) -> None:
        pass
