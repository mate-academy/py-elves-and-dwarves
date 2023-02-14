from abc import ABC, abstractmethod


class Player:
    def __init__(self, nickname) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(Player):

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")

    def player_info(self) -> None:
        pass

    def get_rating(self) -> None:
        pass


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def player_info(self) -> None:
        pass

    def get_rating(self) -> None:
        pass


class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str, bow_level: int):
        super().__init__(nickname=nickname, musical_instrument=musical_instrument)
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self):
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str, favourite_spell: str):
        super().__init__(nickname=nickname, musical_instrument=musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favourite_spell}"

    def get_rating(self):
        return len(self._favourite_spell)


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self):
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"

    def get_rating(self):
        return self._skill_level

