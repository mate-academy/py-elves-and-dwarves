
class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")




class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        super().__init__(
            nickname=nickname,
            favourite_dish=favourite_dish
        )
        self._hummer_level = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> None:
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level")


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        super().__init__(
            nickname=nickname,
            favourite_dish=favourite_dish
        )
        self._skill_level = skill_level

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level")


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(team: list[Elf]) -> int:
    return sum(player.play_elf_song() for player in team)


def feast_of_the_dwarves(team: list[Dwarf]) -> int:
    return sum(player.eat_favourite_dish() for player in team)
