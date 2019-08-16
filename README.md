# Project Pallor

A game where you collect treasure, fight monsters and avoid traps as you try to escape a dark cave.

### Index

* [Release notes](https://github.com/Malodreth/Pallor#release-notes)
* [Getting started](https://github.com/Malodreth/Pallor#getting-started)
    * [Installation](https://github.com/Malodreth/Pallor#installation)
    * [Troubleshooting](https://github.com/Malodreth/Pallor#troubleshooting)
* [How to Play](https://github.com/Malodreth/Pallor#how-to-play)
* [Built With](https://github.com/Malodreth/Pallor#built-with)
* [Author(s)](https://github.com/Malodreth/Pallor#authors)
* [Acknowledgements](https://github.com/Malodreth/Pallor#acknowledgements)


## Release notes

#### Version 0.1.4
###### Release date: 05/14/2017 

* **General**
  
    - Each iteration of the game loop can now load a random pre-generated map
        - Renamed `map.txt` and added 2 new maps for testing. 
        - **Dev note:** *Random selection is disabled by default and is only intended for testing in its current form. To unlock, simply set the `map_id` variable in `main.py` to `pylon.map_select(3)`*
    - Removed `pkg_resources` module from `pylon.py` so that it no longer conflicts with tools like cx_Freeze or pyinstaller
    - Added `setup.py` and reorganised the source code for distribution
    - Readded `pause` to `Pallor.bat` as its only intended purpose now is for development
    - Built `main.exe` included it with the `prerelease_0.1.4` package
        - Windows users can now enjoy play-testing Pallor without installing Python 3.x or any other dependencies
          by downloading and unzipping `prerelease_0.1.4.zip`. Double-click `main.exe` to launch the game


## Getting started

*Currently only supports Windows operating systems.*

### Installation

* ***For players***: **[[Click here]](https://github.com/Malodreth/Pallor/releases/download/v0.1.4/prerelease_0.1.4.zip)** to download the latest `prerelease_x.x.x.zip`. Extract the folder and double-click `main.exe` to launch the game.

* ***For developers***: Simply clone or fork the `master` branch. For your convenience, `Pallor.bat` is included in the `/src` directory as a quicklaunch for testing. Otherwise, open the `cmd` console, `cd` to `/src` and use `python main.py` to run the programme.
    * **Dev note**: *Not compatible with Python 2.x*

### Troubleshooting

###### (for Players)
* **I'm having issues downloading `prerelease_x.x.x.zip`**
    * Some security tools block downloads from unknown publishers. 
        * *In most cases, you can override this by selecting 'Keep File' or 'Continue Anyway'.*
* **`main.exe` isn't opening** or **I'm getting a warning when I try to run `main.exe`**
    * Some security tools block `.exe` files from executing. 
        * *To override this: right-click on the file < go to `Properies` < checkmark `Unblock` < click `Apply`.*

###### (for Developers)
* **`Pallor.bat` isn't opening** 
    * Some security tools block `.bat` files from executing. 
        * *To override this: right-click on the file < go to Properties < check 'Unblock' under Security < click Apply.*
* **I keep getting `'python' is not recognized as an internal or external command`...**
    * If you're launching the programme from `Pallor.bat`, make sure that Python is configured properly. To check this: open the `cmd` console < type `python -V` < hit `Enter`. 
        * *You should see `python x.x.x`, otherwise read **section 3.3 Configuring Python** of the [Python documentation](https://docs.python.org/3.6/using/windows.html) to learn how to manually set your environment variables.*


## How to Play

Choose from the list of available actions in each room to explore the dungeon map:
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
		    ~ The dungeon map is partitioned into several blocks listed north to south.
                      Each block has 5 rows listed west to east. Unexplored areas of the map are
                      labelled '??????????' and become uncovered as you move through the dungeon.
        [ENTER] = Do nothing
```

## Built With

* **Python 3.4.4** [[Download]](https://www.python.org/downloads/)
* **cx_Freeze 5.0.1** [[Download]](https://pypi.python.org/pypi/cx_Freeze)


## Author(s)

* Malodreth
    * **E-mail**: [malodreth@gmail.com](mailto:malodreth@gmail.com)
    * **Website**: [Malodreth's Lair](http://www.malodreth.cf/)
* Phillip Johnson
    * **Website**: [Let's Talk Data](http://letstalkdata.com)


## Licence

This material is covered under the **MIT licence**. 
###### See [License.md](https://github.com/Malodreth/Pallor/blob/master/License.md) for more information.


# Acknowledgements

* Phillip Johnson - [Text Adventure Tutorial](https://github.com/phillipjohnson/text-adventure-tut)
* Typedeaf - [Text Adventure Tutorial (*Typedeaf Fork*)](https://github.com/typedeaf/text-adventure-tut)
