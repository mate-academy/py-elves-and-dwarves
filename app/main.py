from abc import ABC, abstractmethod


# ===== Base Classes =====
class Player(ABC):
    def __init__(self, nickname: str):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str):
        super().__init__(nickname)
        self.musical_instrument = musical_instrument)

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str):
        super().__init__(nickname)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")


# ===== Elf Subclasses =====
class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str, bow_level: int):
        super().__init__(nickname, musical_instrument)
        self.bow_level = bow_level

    def get_rating(self) -> int:
        return self.bow_level * 3

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self.bow_level} level"


class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str, favourite_spell: str):
        super().__init__(nickname, musical_instrument)
        self.favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self.favourite_spell)

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}"


# ===== Dwarf Subclasses =====
class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int):
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level

    def get_rating(self) -> int:
        return self.hummer_level + 5

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level"


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int):
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def get_rating(self) -> int:
        return self.skill_level

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level"


# ===== Functions =====
def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
