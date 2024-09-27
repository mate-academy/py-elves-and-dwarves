"""
This is the base class, which provides basic
information about each player, whether it is
an elf or a dwarf. It is a parent class for
specific classes of elves or dwarves classes,
and have to be inherited by them. Methods are
abstract and do not contain any code to perform,
so each of them must be implemented in a specific
child class.
"""


from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
