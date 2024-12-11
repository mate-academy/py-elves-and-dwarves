from abc import ABC, abstractmethod


class Player(ABC):
    #  which should have a single nickname attribute,
    #  where the player's name will be stored
    # Is this about class attribute or instance att????
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
