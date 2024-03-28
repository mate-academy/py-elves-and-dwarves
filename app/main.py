from abc import abstractmethod, ABC


class Player:
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(ABC, Player):
    def __init__(self, nickname, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a"
              f" song on the {self._musical_instrument}")


class Dwarf(ABC, Player):
    def __init__(self, favourite_dish: str) -> None:
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    def __init__(self, bow_level: int) -> None:
        self._bow_level = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} has"
                f" bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(self, nickname, musical_instrument, favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. {self.nickname} has a"
                f" favourite spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int) -> None:
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. {self.nickname}"
                f" has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int) -> None:
        self._skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} with"
                f" skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level


def calculate_team_total_rating(team: Player) -> None:
    total_rating = 0
    for player in team:
        total_rating += sum(player.get_rating())


def elves_concert(elfs: Elf) -> None:
    for elv in elfs:
        elv.play_elf_song()


def feast_of_the_dwarves(drawfers: Dwarf) -> None:
    for draw in drawfers:
        draw.eat_favourite_dish()
