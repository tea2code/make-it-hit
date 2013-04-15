import sys
from cx_Freeze import setup, Executable

includefiles = ['default-config.yaml', 'levels', 'README.md']
excludes = []
packages = []

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = 'Make-It-Hit',
    version = '3',
    description = 'A little game where you must shoot objects to targets.',
    author = 'tea2code',
    url = 'https://github.com/tea2code/make-it-hit',
    options = {'build_exe': {'excludes': excludes, 'packages':packages, 'include_files': includefiles}}, 
    executables = [Executable('make-it-hit.py', base = base)]
)