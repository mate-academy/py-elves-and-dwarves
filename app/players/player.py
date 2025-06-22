from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
