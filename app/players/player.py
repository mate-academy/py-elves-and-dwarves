from abc import ABC, abstractmethod


class Player(ABC):
    """
    Standard base class for all playable races in the game.

    This class defines the common attributes and methods that every
    character must implement.
    """

    def __init__(
        self,
        nickname: str
    ) -> None:
        """
        Initializes a new playable character.

        Args:
            nickname (str): Alias for the player.
        """
        self.nickname = nickname

    @abstractmethod
    def get_rating(
        self
    ) -> int:
        """
        Calculates and returns the character's power rating.

        Returns:
            int: The calculated rating value.
        """
        pass

    @abstractmethod
    def player_info(
        self
    ) -> str:
        """
        Returns a formatted string with the character's full information.

        Returns:
            str: Brief description and stats of the player.
        """
        pass
