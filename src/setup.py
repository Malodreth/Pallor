import sys
from cx_Freeze import setup, Executable

include_files = ['autorun.inf',
                 'map_1.txt',
                 'map_2.txt',
                 'map_3.txt']

base = "Console"

setup(name="Pallor",
      version="0.1.4",
      description="A game where you collect treasure, fight monsters and avoid traps as you try to escape a dark cave.",
      author="Malodreth",
      options={'build_exe': {'include_files': include_files}},
      executables=[Executable("main.py", base=base, icon="pallor_icon.ico")])
