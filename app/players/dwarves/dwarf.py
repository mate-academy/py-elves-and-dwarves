from players.player import Player


class Dwarf(Player):
    # All dwarves like delicious food so
    # `Dwarf` `__init__` method should take an a
    # dditional argument `favourite_dish` -
    # and stored it in the **protected** attribute.
    # Also, it should have a method `eat_favourite_dish`
    # that should print the following string:
    # `"{nickname} is eating {favourite_dish}"`

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
