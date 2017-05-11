# Project Pallor

A game where you collect treasure, fight monsters and avoid traps as you try to escape a dark cave.

## Patch Notes

```
version 0.1.2 | release date 05/11/2017

* General
  
    - Cleaned up source code in some areas
    - Changed original placement of some lines of text
    - You can now exit from within the game at almost any point by typing 'exit' or 'stop'
    - Added a minor introduction with simple player creation
    - Added a 'restart' function to the end of the game loop
    - Removed 'pause' from Pallor.bat

* Gameplay

    - NEW FEATURE: Stealth! 
        ~ You are now skilled in the art of stealth. When entering a room with an enemy, a stealth check 
          (modified by an enemy's advantage) determines whether you can sneak up on the enemy. If the enemy 
          beats your stealth check with a high perception stat, then you are detected and immediately attacked
    - Added new stats: Perception, Advantage and Stealth
        ~ Perception is an enemy stat that is played against your stealth skill to determine whether stealth is 
          a success or a failure
        ~ Enemies gain advantage when you flee, or attempt to flee, from stealth or combat. Advantage acts as a 
          penalty during a stealth check. Each subsequent attempt to flee or stealth becomes more difficult as 
          the enemy gains advantage, eventually rendering the ability to stealth or flee impossible
        ~ See NEW FEATURE: Stealth 
    - Added new action: 'check status'
        ~ Shows a breakdown of your character, including HP and skills
    - Modified action: flee
        ~ Successful flees from combat increase an enemy's advantage
        ~ Stealthed flees increase an enemy's advantage at 2x the normal amount
```

## Getting Started

Notice: ***REQUIRES** Python 3.x to run!* [Click here](https://www.python.org/downloads/) to download.

*Currently only supports Windows operating systems.*

### Installing

Simply clone the parent folder, then open and double-click Pallor.bat to launch the game.

### Troubleshooting

* **Pallor.bat isn't opening** 
  * Some security tools block .bat files from executing. *To override this: right-click on the file > go to properties > check 'Unblock' under Security > click apply.*
* **I keep getting "*'python' is not recognized as an internal or external command...*"**
  * If you're launching the programme from Pallor.bat, make sure that Python is configured properly. To check this: open the cmd console > type 'python -V' > hit enter. *If you get an error, read section 3.3 Configuring Python of the [Python documentation](https://docs.python.org/3.6/using/windows.html) to learn how to manually set your environment variables.*

## How To Play

Choose from the list of available actions in each room to explore or advance:
```
* Movement: [n] = Go north    [e] = Go east
            [s] = Go south    [w] = Go west

* Combat:   [a] = Attack      [f] = Flee

* Default:  [l] = Look
            [h] = Check status
            [c] = Use consumable 
            [i] = View inventory
            [m] = View Map
		    ~ The dungeon map is broken up into several blocks listed north to south.
                      Each block has 5 rows listed west to east. Unexplored areas of the map are
                      labelled '??????????' and become uncovered as you move through the dungeon. 
        [ENTER] = Do nothing
```
## Built With

* [Python 3.5.3](https://docs.python.org/3.5/whatsnew/3.5.html)

## Author(s)

* **Malodreth** - [Malodreth's Lair](http://www.malodreth.cf/) - [malodreth@gmail.com](mailto:malodreth@gmail.com)

## Licence

This material is covered under the MIT licence. Please see [License.md](https://github.com/Malodreth/Pallor/blob/master/License.md) for more information.

# Acknowledgements

* Phillip Johnson - [Text Adventure Tutorial](https://github.com/phillipjohnson/text-adventure-tut)
* Typedeaf - [Text Adventure Tutorial (*Typedeaf Fork*)](https://github.com/typedeaf/text-adventure-tut)