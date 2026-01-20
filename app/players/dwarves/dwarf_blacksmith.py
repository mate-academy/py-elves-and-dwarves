from players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    # `DwarfBlacksmith` should be a child of `Dwarf`.
    # Its `__init__` method should take one additional parameter:
    # `skill_level` - an integer that shows the level of blacksmith's skills.
    # The `__init__` method should store it in the protected attribute.
    def __init__(self, nickname: str,
                 favourite_dish: str, skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self) -> int:
        # `get_rating` method should return:
        # * `skill_level` for `DwarfBlacksmith`
        return self._skill_level

    def player_info(self) -> str:
        # * `"Dwarf blacksmith {nickname} with skill of
        # the {skill_level} level"` for `DwarfBlacksmith` instances
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self._skill_level} level")
