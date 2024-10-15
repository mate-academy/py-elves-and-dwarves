from abc import ABC, abstractmethod


class Player(ABC):
    team = []

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        Player.team.append(self)

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
