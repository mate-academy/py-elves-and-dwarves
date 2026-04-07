from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(
            self,
            nickname: str
    ) -> None:
        self.nickname = nickname

    @abstractmethod
    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}."
                f" {self.nickname} has bow of the {self._bow_level} level")

    @abstractmethod
    def get_rating(self) -> int:
        return 3 * self._bow_level
