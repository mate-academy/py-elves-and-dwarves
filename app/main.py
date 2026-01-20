from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass


class Elf(Player):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")


class Dwarf(Player):
    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    def __init__(self, nickname, musical_instrument, bow_level):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self):
        return 3 * self._bow_level

    def player_info(self):
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )


class Druid(Elf):
    def __init__(self, nickname, musical_instrument, favourite_spell):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self):
        return len(self._favourite_spell)

    def player_info(self):
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: {self._favourite_spell}"
        )


class DwarfWarrior(Dwarf):
    def __init__(self, nickname, favourite_dish, hummer_level):
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def get_rating(self):
        return self._hummer_level + 4

    def player_info(self):
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the {self._hummer_level} level"
        )


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, favourite_dish, skill_level):
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def get_rating(self):
        return self._skill_level

    def player_info(self):
        return (
            f"Dwarf blacksmith {self.nickname} "
            f"with skill of the {self._skill_level} level"
        )


def calculate_team_total_rating(team):
    return sum(player.get_rating() for player in team)


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
