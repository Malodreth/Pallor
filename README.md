# Project Pallor

A game where you collect treasure, fight monsters and avoid traps as you try to escape a dark cave.

## Patch Notes

```
version 0.1.3 | release date 05/12/2017

* General
  
    - Cleaned up redundancies in source code for better optimisation and reorganised for legibility
    - Added loops in some areas to handle unwanted user input    

* Gameplay

    - NEW FEATURE: Locked items! 
        ~ Treasure isn't as exciting when it's just handed to you. Now you can find locked doors, chests,
          and more on your journey. You'll have to find the right key, but who knows what - or who! - could 
          be locked inside?!
    - Added new room class: Locked Rooms 
    - Added new item class: Keys
    - Added new action: 'Use key'
    - Added new items: Longsword, Golden Key and Bone Key
    - Updated map.txt with new rooms and altered layout
    - Made slight changes to enemies:
        ~ Ogres now have considerably more health: Up by 100% (was 30 HP)
        ~ Giant Spiders have 50% more health and base damage (was 10 HP and 2 damage, respectively)    
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
            [k] = Use key
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

* Malodreth | ***Website:*** [Malodreth's Lair](http://www.malodreth.cf/) | ***E-mail:*** [malodreth@gmail.com](mailto:malodreth@gmail.com)

## Licence

This material is covered under the **MIT licence**. Please see [License.md](https://github.com/Malodreth/Pallor/blob/master/License.md) for more information.

# Acknowledgements

* Phillip Johnson - [Text Adventure Tutorial](https://github.com/phillipjohnson/text-adventure-tut)
* Typedeaf - [Text Adventure Tutorial (*Typedeaf Fork*)](https://github.com/typedeaf/text-adventure-tut)