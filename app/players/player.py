from abc import abstractmethod, ABC


class Player(ABC):
    players = []

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        Player.players.append(self.nickname)

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
