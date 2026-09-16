from abc import abstractmethod

class Player:
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass

class Elf(Player):
    def __init__(self, musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song \
        on the {self._musical_instrument}")

class Dwarf(Player):
    def __init__(self, favourite_dish: str) -> None:
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")

class ElfRanger(Elf):
    pass


class Druid(Elf):
    pass


class DwarfWarrior(Dwarf):
    pass


class DwarfBlacksmit(Dwarf):
    pass
