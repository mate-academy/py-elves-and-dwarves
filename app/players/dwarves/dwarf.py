from app.players.player import Player


class Dwarf(Player):
    """
    The abstract Dwarf class.

    Attributes:
    ___________
    nickname
        the name of the Elf
    favourite_dish
        the Dwarf's favorite dish

    Methods:
    _______
    get_rating()
        the abstractmethod

    player_info()
        the abstractmethod

    eat_favorite_dish()
        displays a message about eating a favorite dish
    """
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        """
        Displays a message about eating a favorite dish.
        :return: None
        """
        print(f"{self.nickname} is eating {self._favourite_dish}")
