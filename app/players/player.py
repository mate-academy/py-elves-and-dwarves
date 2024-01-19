from abc import abstractmethod, ABC


class Player(ABC):

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
