from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, skill_level: int) -> str:
        self._skill_level = skill_level

    @abstractmethod
    def player_info(self) -> str:
        pass

    @abstractmethod
    def get_rating(self) -> int:
        pass
