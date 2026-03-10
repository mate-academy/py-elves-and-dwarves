from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract base class for all players in the meta universe."""
    def __init__(
            self,
            nickname: str
    ) -> None:
        """Initialize a player with a nickname."""
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Abstract method to get the player's rating."""
        pass

    @abstractmethod
    def player_info(self) -> str:
        """Abstract method to get the player's information."""
        pass
