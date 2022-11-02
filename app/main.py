from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elves(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a \
        song on the {self._musical_instrument}")

    def player_info(self) -> None:
        pass

    def get_rating(self) -> int:
        pass


class Dwarves(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def player_info(self) -> None:
        pass

    def get_rating(self) -> int:
        pass


class ElfRanger(Elves):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> None:
        print(
            f"Elf ranger {self.nickname}. \
            {self.nickname} has bow of the {self._bow_level} level"
        )

    def get_rating(self) -> int:
        return self._bow_level * 3


class Druid(Elves):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 favourite_spell: str
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> None:
        print(
            f"Druid {self.nickname}. \
            {self.nickname} has a favourite spell: {self._favourite_spell}"
        )

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class DwarfWarrior(Dwarves):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 hummer_level: int
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._hummer_level = hummer_level

    def player_info(self) -> None:
        print(
            f"Dwarf warrior {self.nickname}. \
            {self.nickname} has a hummer of the {self._hummer_level} level"
        )

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarves):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 skill_level: int
                 ) -> None:
        super().__init__(nickname, musical_instrument)
        self._skill_level = skill_level

    def player_info(self) -> None:
        print(
            f"Dwarf blacksmith {self.nickname} \
            with skill of the {self._skill_level} level"
        )

    def get_rating(self) -> int:
        return self._skill_level
