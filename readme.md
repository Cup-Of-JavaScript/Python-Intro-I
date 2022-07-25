# Python Intro - I
Introduction into Python.

Assignments are located [here](assignments.md).

# Getting Started
- Clone this repo into a new directory
- Open this directory with Intellij:
  - File >> Open >> python-intro-I
- Open Terminal window (click on Terminal tab at bottom of IntelliJ)
- Create virtual environment: `python -m venv venv`
- Activate virtual environment: `venv\Scripts\activate.bat`
- Install dependecies: `pip install -r requirements.txt`
- Create a new file called `main.py`
- Copy contents of `main.py.template` to `main.py`
- Update `main.py` with your student id
- Edit Configurations... (left of green arrow)
  - Script path: `C:\vc\gitlab\python-intro-I\python-intro-I\main.py`
  - Use specified interpreter: `Python 3.10`
- Press green "play" button at top of IntelliJ 
- Observe `TODO: Ex. 1...` in the terminal window

# Data Types
- Text Type: `str`
- Numeric Types: `int`, `float`, `complex`
- Sequence Types:	`list`, `tuple`, `range`
- Mapping Type: `dict`
- Set Types: `set`, `frozenset`
- Boolean Type: `bool`
- Binary Types: `bytes`, `bytearray`, `memoryview`
- None Type: `NoneType`

# Call by Value vs Call by Reference
- Mutable types are passed by reference
- Immutable types are passed by value (AKA copy)
- Mutable types:
  - Lists
  - Dictionaries
  - Sets
- Immutable types:
  - Integers
  - Floats
  - Booleans
  - Strings
  - Tuples
  - Frozenset

# Videos
- [Python for Beginners - Mosh (60m)](https://youtu.be/kqtD5dpn9C8)
- [venv (17m)](https://youtu.be/APOPm01BVrk)

# Links
- [W3 Schools](https://www.w3schools.com/python/python_intro.asp)
- [String Slicing](https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3)
