from abc import ABC, abstractmethod

# Imagine that you have started developing your meta universe.
# In your universe, all players are
# divided into two races - `Elves` and `Dwarves`.
# Both races are divided into two groups.
# For elves, these are the `ElfRanger` and `Druid` classes.
# Dwarves have the `DwarfWarrior` and `DwarfBlacksmith` classes.

# Thus, each player should be an instance of one of these four classes.
# But to have better code design, you should
# implement the abstract classes `Elf`, `Dwarf` and `Player`,
# where you can put the common logic.


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
    # The base class should be the `Player` class,
    # which should have a single `nickname`
    # attribute, where the player's name will be stored.
    # It must also have two empty abstract
    # methods `get_rating`, `player_info`, declared,
    # thus we guarantee that all players
    # in our universe will have them defined.

    @abstractmethod
    def get_rating(self) -> None:
        # `get_rating` method should return:
        # * 3 * `bow_level` for `ElfRanger`
        # * length of `favourite_spell` for `Druid`
        # * `hummer_level` + 4 for `DwarfWarrior`
        # * `skill_level` for `DwarfBlacksmith`
        pass

    @abstractmethod
    def player_info(self) -> None:
        # `player_info` method should return:
        pass

    # Two classes `Elf` and `Dwarf` should be inherited from the `Player`.
