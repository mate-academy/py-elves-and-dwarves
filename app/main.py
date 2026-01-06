from abc import ABC, abstractmethod

#Гравець
class Player(ABC):
    nickname = ""


    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass


#Ельф
class Elf(Player):
    def __init__(self, nickname, musical_instrument):
        self._musical_instrument = musical_instrument

    def palay_elf_song(self):
        return f"{nickname} is playing a song on the {self._musical_instrument}"


class ElfRanger(Elf):
    def __init__(self, bow_level):
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {nickname}. {nickname} has bow of the {bow_level} level"

    def get_rating(self):
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(self, favourite_spell):
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {nickname}. {nickname} has a favourite spell: {self.favourite_spell}"

    def get_rating(self):
        return len(favourite_spell)


#Гноми
class Dwarf(Player):
    def __init__(self, nickname, favorite_dish):
        self._favorite_dish = favorite_dish


    def eat_favorite_dish(self):
        return f"{nicckname} is eating {self.favorite_dish}"


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level):
        self.hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {nickname}. {nickname} has a hummer of the {self.hummer_level} level"

    def get_rating(self):
        return self.hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level):
        self.skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {nickname} with skill of the {self.skill_level} level"

    def get_rating(self):
        return self.skill_level


def calculate_team_total_rating(elf):
    return sum(elf.get_rating())

def elves_concert(elves):
    for elves in elves:
        print(elves.palay_elf_song())

def feast_of_the_dwarves(dwarves):
    for dwarves in dwarves:
        print(dwarves.eat_favorite_dish())