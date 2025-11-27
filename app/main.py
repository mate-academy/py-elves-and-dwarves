from abc import ABC, abstractmethod


# ===== Base Classes =====
class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.musical_instrument}")


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")


# ===== Elf Subclasses =====
class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self.bow_level = bow_level

    def get_rating(self) -> int:
        return self.bow_level * 3

    def player_info(self) -> str:
        return ("Elf ranger {0}. {0} has bow of the {1} level"
                .format(self.nickname, self.bow_level))


class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self.favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return len(self.favourite_spell)

    def player_info(self) -> str:
        return ("Druid {0}. {0} has a favourite spell: {1}"
                .format(self.nickname, self.favourite_spell))


# ===== Dwarf Subclasses =====
class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level

    def get_rating(self) -> int:
        return self.hummer_level + 5

    def player_info(self) -> str:
        return ("Dwarf warrior {0}. {0} has a hummer of the {1} level"
                .format(self.nickname, self.hummer_level))


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def get_rating(self) -> int:
        return self.skill_level

    def player_info(self) -> str:
        return ("Dwarf blacksmith {0} with skill of the {1} level"
                .format(self.nickname, self.skill_level))


# ===== Functions =====
def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
