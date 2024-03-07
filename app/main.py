from abc import abstractmethod, ABC


class Player(ABC):

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(Player):

    def __init__(self, musical_instrument: str, nickname: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


class Dwarf(Player):

    def __init__(self, favorite_dish: str, nickname:str) -> None:
        super().__init__(nickname)
        self._favorite_dish = favorite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favorite_dish}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


class ElfRanger(Elf):
    def __init__(self, bow_level: int, musical_instrument: str, nickname: str):
        super().__init__(musical_instrument, nickname)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3*self._bow_level


class Druid(Elf):
    def __init__(self, favorite_spell: str, musical_instrument: str, nickname: str) -> None:
        super().__init__(musical_instrument, nickname)
        self._favorite_spell = favorite_spell

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favorite_spell}"

    def get_rating(self) -> int:
        return len(self._favorite_spell)


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int, favorite_dish: str, nickname: str) -> None:
        super().__init__(favorite_dish, nickname)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int, favorite_dish: str, nickname: str) -> None:
        super().__init__(favorite_dish, nickname)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level

