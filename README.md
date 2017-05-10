# Project Pallor

A game where you collect treasure, fight monsters and avoid traps as you try to escape a dark cave.

## Patch Notes

```
version 0.1.0 | release date 05/09/2017

* Initial release
```

## Getting Started

Notice: ***REQUIRES** Python 3.x to run!* [Click here](https://www.python.org/downloads/) to download.

### Installing

Simply clone the parent folder, then open and double-click Pallor.bat to launch the game.

###Troubleshooting

* **Pallor.bat isn't opening** 
 * Some security tools block .bat files from executing. *To override this: right-click on the file > go to properties > check 'Unblock' under Security > click apply.*
* **I keep getting "*'python' is not recognized as an internal or external command...*"**
 * If you're launching the programme from Pallor.bat, make sure that Python is configured properly. To check this: open the cmd console > type 'python -V' > hit enter. *If you get an error, read section 3.3 Configuring Python of the [Python documentation](https://docs.python.org/3.6/using/windows.html) to learn how to manually set your environment variables.*

## How To Play

Choose from the list of available actions in each room to explore or advance:
```
* Movement: [n] = Go north   [e] = Go east
            [s] = Go south   [w] = Go west

* Combat:   [a] = Attack     [f] = Flee

* Default:  [i] = View inventory
            [m] = View Map
		  - The dungeon map is broken up into several blocks listed north to south.
                    Each block has 5 rows listed west to east. Unexplored areas of the map are
                    labelled '??????????' and become uncovered as you move through the dungeon. 
        [ENTER] = Do nothing
```
## Built With

* [Python 3.5.3](https://docs.python.org/3.5/whatsnew/3.5.html)

## Author(s)

* **Malodreth** - [Malodreth's Lair](http://www.malodreth.cf/) - [malodreth@gmail.com](mailto:malodreth@gmail.com)

## Licence

Check back later for more info.

# Acknowledgements

* Phillip Johnson - [Text Adventure Tutorial](https://github.com/phillipjohnson/text-adventure-tut)
* Typedeaf - [Text Adventure Tutorial (*Typedeaf Fork*)](https://github.com/typedeaf/text-adventure-tut)