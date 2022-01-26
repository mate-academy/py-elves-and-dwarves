# Python boilerplate for GitHub tasks

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Imagine that you have started developing your meta universe.
In your universe, all players are divided into two races - `Elves` and `Dwarves`. 
Both races are divided into two groups. For elves, these are the `ElfRanger` and `Druid` classes. 
Dwarves have the `DwarfWarrior` and `DwarfBlacksmith` classes.

Thus, each player should be an instance of one of these four classes.
But to have better code design, you should implement the abstract classes `Elf`, `Gnome` and `Player`, 
where you can put the common logic.

The base class should be the `Player` class, 
which should have a single `nickname` attribute, where the player's name will be stored. 
It must also have two empty abstract methods `get_rating`, `player_info`, declared, 
thus we guarantee that all players in our universe will have them defined.

Two classes `Elf` and `Dwarf` should be inherited from the `Player`.

All elves like playing songs so
`Elf` constructor should take an additional argument `musical_instrument` -  and stored it in the **protected** attribute.
Also, it should have a method `play_elf_song` that should print the following string:
`"{nickname} is playing a song on the {musical_instrument}"`

All dwarves like delicious food so
`Dwarf` constructor should take an additional argument `favourite_dish` -  and stored it in the **protected** attribute.
Also, it should have a method `eat_favourite_dish` that should print the following string:
`"{nickname} is eating {favourite_dish}"`

Finally, create four classes: `ElfRanger`, `Druid`, `DwarfWarrior` and `DwarfBlacksmith`.

`ElfRanger` should be a child of `Elf`.
Its constructor should take one additional parameter: 
`bow_level` - an integer that shows the quality of the bow.
Constructor should store it in the protected attribute.

`Druid` should be a child of `Elf`.
Its constructor should take one additional parameter: 
`favourite_spell` - the text of the favourite spell.

`DwarfWarrior` should be a child of `Dwarf`.
Its constructor should take one additional parameter: 
`hummer_level` - an integer that shows the power of the hummer.

`DwarfBlacksmith` should be a child of `Dwarf`.
Its constructor should take one additional parameter: 
`skill_level` - an integer that shows the level of blacksmith's skills.

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
* `skill_level` + 4 for `DwarfBlacksmith`


Write following functions:
* `calculate_team_total_rating` - 
it should take list of `Player`s and return the sum of the ratings for all team members
* `elves_concert` - it should take a list of `Elf` and call `play_elf_song` method for each elf.
* `feast_of_the_dwarves` - it should take a list of `Dwarf` and call `eat_favourite_dish` method for each dwarf.