from abc import abstractmethod, ABC


class Player(ABC):

    nickname = ""

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
