from app.players.player import Player
from app.players.elves.elf import Elf


def calculate_team_total_rating(team_members: list[Player]):
    return sum([member.get_rating() for member in team_members])

def elves_concert(elves: list[Elf]):
    for elf in elves:
        elf.play_elf_song()
