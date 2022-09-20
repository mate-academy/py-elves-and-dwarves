from abc import ABCMeta, abstractmethod

from app.players.player import Player


# metaclass=ABCMeta makes IDE recognize that this is also an abstract class.
class Dwarf(Player, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
