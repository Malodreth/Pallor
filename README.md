# Project Pallor

A game where you collect treasure, fight monsters and avoid traps as you try to escape a dark cave.


## Patch Notes

```
version 0.1.4 | release date 05/14/2017

* General
  
    - Each iteration of the game loop now loads a random pre-generated map
        ~ Renamed map.txt and added 2 new maps for testing. Dev note: Random selection is disabled
          by default and is only intended for testing in its current form. To unlock, simply set the
          'map_id' variable in main.py to 'pylon.map_select(3)'
    - Removed pkg_resources module from 'pylon.py' so that it no longer conflicts with various resourcing tools
    - Added 'setup.py' and reorganised the source code to prep for distribution
    - Readded 'pause' to Pallor.bat as its only intended purpose now is for development
    - Built 'main.exe' included with 'prerelease_0.1.4' package
        ~ Windows users can now enjoy playtesting Pallor without installing Python 3.x or any other dependencies
          by downloading and unzipping 'prerelease_0.1.4'. Double-click 'main.exe' to launch the game
          WARNING: May be unstable on some versions of Windows. Use at your own risk!   
```


## Getting Started

***WARNING***: May be unstable on some versions of Windows. *Use at your own risk!*

*Currently only supports Windows operating systems.*

### Installing

[Click here](https://github.com/Malodreth/Pallor/releases/download/v0.1.4/prerelease_0.1.4.zip) to download '***prerelease_x.x.x.zip***', then extract the folder and double-click '*main.exe*' to launch the game.


### Troubleshooting

* **I'm having issues downloading '*prerelease_x.x.x*'...**
    * Some security tools block downloads from unknown publishers. 
        * *In most cases, this can be overridden by selecting 'Keep File'.*
* **'*main.exe*' isn't opening**
    * As before, some security tools block .exe files from executing. 
        * *To override this: right-click on the file < go to Properies < check 'Unblock' under Security < click Apply.*

###### (for Developers)
* **'*Pallor.bat*' isn't opening** 
    * Some security tools block .bat files from executing. 
        * *To override this: right-click on the file < go to Properties < check 'Unblock' under Security < click Apply.*
* **I keep getting "*'python' is not recognized as an internal or external command...*"**
    * If you're launching the programme from Pallor.bat, make sure that Python is configured properly. To check this: open the cmd console < type 'python -V' < hit enter. 
        * *If you continue to get an error, read section 3.3 Configuring Python of the [Python documentation](https://docs.python.org/3.6/using/windows.html) to learn how to manually set your environment variables.*


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

* Python 3.4.4 and 3.5.3 [Download](https://www.python.org/downloads/)


## Author(s)

* Malodreth | ***Website:*** [Malodreth's Lair](http://www.malodreth.cf/) | ***E-mail:*** [malodreth@gmail.com](mailto:malodreth@gmail.com)


## Licence


This material is covered under the **MIT licence**. Please see [License.md](https://github.com/Malodreth/Pallor/blob/master/License.md) for more information.


# Acknowledgements

* Phillip Johnson - [Text Adventure Tutorial](https://github.com/phillipjohnson/text-adventure-tut)
* Typedeaf - [Text Adventure Tutorial (*Typedeaf Fork*)](https://github.com/typedeaf/text-adventure-tut)