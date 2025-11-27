from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, nickname: str):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass

class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str):
        super().__init__(nickname)
        self.musical_instrument = musical_instrument

    @abstractmethod
    def play_elf_song(self):
        pass

class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str):
        super().__init__(nickname)
        self.favourite_dish = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self):
        pass

class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str, bow_level: int):
        super().__init__(nickname, musical_instrument)
        self.bow_level = bow_level

    def get_rating(self):
        return self.bow_level * 3

    def player_info(self):
        return (
            f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
            f"{self.bow_level} level"
        )

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")

class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str, favourite_spell: str):
        super().__init__(nickname, musical_instrument)
        self.favourite_spell = favourite_spell

    def get_rating(self):
        return len(self.favourite_spell) + 2

    def player_info(self):
        return (
            f"Druid {self.nickname}. {self.nickname} has a favourite spell: "
            f"{self.favourite_spell}"
        )

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")

class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, hummer_level: int):
        super().__init__(nickname, favourite_dish)
        self.hummer_level = hummer_level

    def get_rating(self):
        return self.hummer_level + 5

    def player_info(self):
        return (
            f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of "
            f"the {self.hummer_level} level"
        )

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.favourite_dish}")

class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int):
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def get_rating(self):
        return self.skill_level

    def player_info(self):
        return (
            f"Dwarf blacksmith {self.nickname} with skill of the "
            f"{self.skill_level} level"
        )

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.favourite_dish}")

def calculate_team_total_rating(team):
    return sum(player.get_rating() for player in team)

def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
