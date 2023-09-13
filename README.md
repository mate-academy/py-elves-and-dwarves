# Elves and Dwarves

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

Imagine that you have started developing your meta universe.
In your universe, all players are divided into two races - `Elves` and `Dwarves`. 
Both races are divided into two groups. For elves, these are the `ElfRanger` and `Druid` classes. 
Dwarves have the `DwarfWarrior` and `DwarfBlacksmith` classes.

Thus, each player should be an instance of one of these four classes.
But to have better code design, you should implement the abstract classes `Elf`, `Dwarf` and `Player`, 
where you can put the common logic.

The base class should be the `Player` class, 
which should have a single `nickname` attribute, where the player's name will be stored. 
It must also have two empty abstract methods `get_rating`, `player_info`, declared, 
thus we guarantee that all players in our universe will have them defined.

Two classes `Elf` and `Dwarf` should be inherited from the `Player`.

All elves like playing songs so
`Elf` `__init__` method should take an additional argument `musical_instrument` -  and stored it in the **protected** attribute.
Also, it should have a method `play_elf_song` that should print the following string:
`"{nickname} is playing a song on the {musical_instrument}"`

All dwarves like delicious food so
`Dwarf` `__init__` method should take an additional argument `favourite_dish` -  and stored it in the **protected** attribute.
Also, it should have a method `eat_favourite_dish` that should print the following string:
`"{nickname} is eating {favourite_dish}"`

Finally, create four classes: `ElfRanger`, `Druid`, `DwarfWarrior` and `DwarfBlacksmith`.

`ElfRanger` should be a child of `Elf`.
Its `__init__` method should take one additional parameter: 
`bow_level` - an integer that shows the quality of the bow.
The `__init__` method should store it in the protected attribute.

`Druid` should be a child of `Elf`.
Its `__init__` method should take one additional parameter: 
`favourite_spell` - the text of the favourite spell.
The `__init__` method should store it in the protected attribute.

`DwarfWarrior` should be a child of `Dwarf`.
Its `__init__` method should take one additional parameter: 
`hummer_level` - an integer that shows the power of the hummer.
The `__init__` method should store it in the protected attribute.

`DwarfBlacksmith` should be a child of `Dwarf`.
Its `__init__` method should take one additional parameter: 
`skill_level` - an integer that shows the level of blacksmith's skills.
The `__init__` method should store it in the protected attribute.

All of these classes should have implementations of `player_info` and 
`get_rating` methods.

`player_info` method should return:
* `"Elf ranger {nickname}. {nickname} has bow of the {bow_level} level"` for `ElfRanger` instances
* `"Druid {nickname}. {nickname} has a favourite spell: {favourite_spell}"` for `Druid` instances
* `"Dwarf warrior {nickname}. {nickname} has a hummer of the {hummer_level} level"` for `DwarfWarrior` instances
* `"Dwarf blacksmith {nickname} with skill of the {skill_level} level"` for `DwarfBlacksmith` instances


`get_rating` method should return:
* 3 * `bow_level` for `ElfRanger`
* length of `favourite_spell` for `Druid`
* `hummer_level` + 4 for `DwarfWarrior`
* `skill_level` for `DwarfBlacksmith`

```python
ranger = ElfRanger(
    nickname="Nardual Chaekian",
    musical_instrument="flute",
    bow_level=7
)
ranger.get_rating() == 21
ranger.player_info() == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
ranger.play_elf_song()  # "Nardual Chaekian is playing a song on the flute" 
```

```python
warrior = DwarfWarrior(
    nickname="Thiddeal",
    favourite_dish="French Fries",
    hummer_level=7
)
warrior.get_rating() == 11
warrior.player_info() == "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
warrior.eat_favourite_dish()  # "Thiddeal is eating French Fries" 
```



Write following functions:
* `calculate_team_total_rating` - 
it should take list of `Player`s and return the sum of the ratings for all team members
```python
team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
calculate_team_total_rating(team) == 102  # 33 * 3 + 3
```
* `elves_concert` - it should take a list of `Elf` and call `play_elf_song` method for each elf.
```python
elves = [
    Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
    ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
]
elves_concert(elves)
# "Nardual is playing a song on the flute"
# "Rothilion is playing a song on the trumpet"
```
* `feast_of_the_dwarves` - it should take a list of `Dwarf` and call `eat_favourite_dish` method for each dwarf.
```python
dwarves = [
    DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
    DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
]
feast_of_the_dwarves(dwarves)
# "Thiddeal is eating French Fries"
# "Dwarf is eating Caesar Salad"
```

Use the following project structure:
```
app/
    main.py
    players/
        player.py
        elves/
            elf.py
            elf_ranger.py
            druid.py
        dwarves/
            dwarf.py
            dwarf_warrior.py
            dwarf_blacksmith.py
```
All classes should be defined in the corresponding modules.
Functions should be defined in the `main.py` module.

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
