from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


class Elf(Player):
    def __init__(self, nickname: str, _musical_instrument: str):
        super().__init__(nickname)
        self._musical_instrument = _musical_instrument

    def play_elf_song(self):
        return f"{self.nickname} is playing a song on the {self._musical_instrument}"


class Dwarf(Player):
    def __init__(self, nickname: str, _favorite_dish: str):
        super().__init__(nickname)
        self._favorite_dish = _favorite_dish

    def eat_favourite_dish(self):
        return f"{self.nickname} is eating {self._favorite_dish}"

class ElfRanger(Elf):
    def __init__(self, nickname: str, _musical_instrument: str, bow_level: int):
        super().__init__(nickname, _musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(self, nickname: str, _musical_instrument: str, _favourite_spell: str):
        super().__init__(nickname, _musical_instrument)
        self._favourite_spell = _favourite_spell

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favourite_spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, _favorite_dish: str, _hummer_level: int):
        super().__init__(nickname, _favorite_dish)
        self._hummer_level = _hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}.{self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, _favorite_dish: str, _skill_level: int):
        super().__init__(self.nickname, self._favorite_dish)
        self._skill_level = _skill_level

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level

    @staticmethod
    def calculate_team_total_rating(players: list) -> int:
        return sum(player.get_rating() for player in players)