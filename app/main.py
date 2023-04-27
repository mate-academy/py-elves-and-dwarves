# meta universe
# players :
# 1. Elves - 1. ElfRanger 2. Druid
# 2. Dwarves - 1. DwarfWarrior 2. DwarfBlacksmith

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
    def testt(self):
        print("TEST")

class Elf(Player):
    def __init__(self, nickname, musical_instrument):
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song"
              f" on the {self._musical_instrument}")

    def get_rating(self):
        pass


    def player_info(self):
        if isinstance(self, Elf):
            if isinstance(self, ElfRanger):
                return (f"Elf ranger {self.nickname}. "
                        f"{self.nickname} has bow of the {self._bow_level} level")
            else:
                return (f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favourite_spell}")


class Dwarf(Player):
    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self._favorite_dish = favourite_dish

    def get_rating(self):
        pass

    def player_info(self):
        if isinstance(self, Dwarf):
            if isinstance(self, DwarfWarrior):
                return (f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level")
            else:
                return (f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level")

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favorite_dish}")




class ElfRanger(Elf):
    def __init__(self, nickname, musical_instrument, bow_level: int):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level


class Druid(Elf):
    def __init__(self, nickname, musical_instrument, favourite_spell : str):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell  = favourite_spell

class DwarfWarrior(Dwarf):
    def __init__(self, nickname, favourite_dish,hummer_level  ):
        super().__init__(nickname, favourite_dish)
        self._hummer_level   = hummer_level
class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname, favourite_dish,skill_level   ):
        super().__init__(nickname, favourite_dish)
        self._skill_level    = skill_level






















elf_test = Elf("Zhora elf", "Violin")
elf_test.play_elf_song()
dwarf_test = Dwarf("Stepa Korotkiy", "M'yaso")
dwarf_test.eat_favourite_dish()
elf_ranger_test = ElfRanger("Sanya","Guitar",32)
print(elf_ranger_test.__dict__)
dudu_test = Druid("Vasyl", "Sopilochka", "Leviossa")
print(dudu_test.__dict__)
korotish_war = DwarfWarrior("Kolya molot", "Pelmen's", 44)
print(elf_ranger_test.player_info())
print(dudu_test.player_info())
korotish_craft = DwarfBlacksmith("Oleg Zavod","Rul'ka", 9000)
print(korotish_craft.player_info())