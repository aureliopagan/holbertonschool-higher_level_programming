## Python - Input/Output

### Resources
Read or watch:
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/library/contextlib.html#context-manager-cleanup)
- [Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))](https://diveintopython3.net/files.html)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8: Reading / Writing Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://automatetheboringstuff.com/)
- [sys package](https://docs.python.org/3/library/sys.html)

### Learning Objectives
By the end of this project, you should be able to explain (without Google):

#### General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
- How to access command line parameters in a Python script

### Requirements

#### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use `pycodestyle` (version 2.7.\*)
- All files must be executable
- File length will be tested using `wc`

#### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed using: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation must be a real sentence explaining the purpose of the module, class, or method (length will be verified)
- Collaboration on test cases is strongly encouraged to cover edge cases