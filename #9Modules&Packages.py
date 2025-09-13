#1 What is using packages and modules a smart idea?
# because when writing big programs it is inpractical to place code for all functions in the same file

#2 What is difference between writing code in interactive vs script mode?
# Interactive mode runs code line by line with immediate output, useful for testing.
# Script mode runs the whole file at once, used to write full programs

#3 What is a file ending with .py calles?
# a module 

#4 How do you starta python program in script-mode, in mac terminal or using IDE?
# Mac terminal: Navigate to your script folder: "cd path/to/your/script" Then run: "python3 file.py"
# IDE: Open your .py file in the IDE. Click the Run button or use shortcut (e.g., Cmd + Shift + F10 in PyCharm). The IDE runs the script in script mode automatically.

#5 What is a "main" module?
# The main module starts the program, that is being run directly by the Python interpreter. Gets the unique name __main__. Other modules organize the code into reusable parts. A program can consist of multiple modules , not just main-module. This makes the program easier to read, test, and maintain.

my_program/
│
├── main.py          # Main module (entry point)
├── math_utils.py    # A helper module
└── string_utils.py  # Another helper module

#6 How to import a module (that solely consists of definitions) to use in another module EX. MAIN-MODULE?
# by using an import-statement using the modules name in program, usualy in the beginning. To call a function defined in the imported module write "modulename.functionname"

#A module can also contain definitions and directly runnable code (when the functions are called upon)

#7 How can you change a modulename during importion (bsc it is too long to write)?
# "import modulname as mn" then call it as "mn.functionname". eg use DOT

#8 How can you import a certain functionname/definition directly?
# from "modulename" import "functionname"

#9 How can you import ALL functions/definitions from a module as once?
# from "modulename" import *

# Everything defined on a global-level is reachable from a module during import, ex. variable-names, lists etc
#module: import sys gives you access to Python's interaction with the system and command line, useful when running scripts in the Mac Terminal or any terminal.
#module: import numpy loads the NumPy library, which is a powerful Python library for numerical computing.

#10 What are direcories, and subdirectories made for?
# to organize files 

#11 What is similarly used in python?
# Instead of directories and files, it is called Packages and Subpackages containing modules (.py files)

#You can use duplicate names for modules as long as they are inside different packages

#12 How is the modules inside a Package (or Subpackage)named during import and usage?
# Modules are named using dot (.) notation, following the folder structure.
# my_package.module1 or my_package.subpackage.module2

#13 Why do we nee to place a __init__.py file inside a python package?
# The __init__.py file is used to mark a folder as a Python package, allowing Python to import its modules properly and optionally run initialization code.

#14 Why does this __init__.py file need to contain a variable called __all__
# The __all__ variable is used to control what gets imported when you use: from package import *
# It defines the public interface of the package — the modules or names that should be exposed when using wildcard imports.
my_package/
├── __init__.py
├── module1.py
├── module2.py

# __init__.py
__all__ = ['module1']

Now if you write: from my_package import *. Only module1 will be imported — module2 will be ignored.


