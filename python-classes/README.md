# Python - Classes and Objects

## Background Context

It is **very important** to read all the material listed below (and skip what is recommended to skip; you will see those later in the curriculum).

As usual, make sure you **type** (never copy and paste), test, and understand all examples shown in the following links (including those in the video). The biggest takeaway from this project is: **experiment with OOP yourself—play with it!**

Read or watch the resources below in the order presented.

## Resources

- **Object Oriented Programming**  
    (Read everything up to, but not including, the “Inheritance” paragraph. You do **not** need to learn about class attributes, `classmethod`, or `staticmethod` yet.)
- **Object-Oriented Programming**  
    (*Be careful*: In most of the following paragraphs, the author demonstrates things you should **not** do when writing a class, to help you better understand concepts and how Python 3 works. Make sure you read these sections: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (skip class attributes), Methods, The `__init__` Method, Data Abstraction, Data Encapsulation, and Information Hiding, Public/Protected/Private Attributes.)
- [Properties vs. Getters and Setters](#)
- [Learn to Program 9: Object Oriented Programming](#)
- [Python Classes and Objects](#)
- [Object Oriented Programming](#)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external help:

### General

- What is OOP (Object-Oriented Programming)
- What does “first-class everything” mean
- What is a class
- What is an object and an instance
- The difference between a class and an object or instance
- What is an attribute
- How to use public, protected, and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What are Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- The difference between an attribute and a property in Python
- The Pythonic way to write getters and setters
- How to dynamically create new attributes for existing instances of a class
- How to bind attributes to objects and classes
- What is the `__dict__` of a class or instance and what it contains
- How Python finds the attributes of an object or class
- How to use the `getattr` function

## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use `pycodestyle` (version 2.7.\*)
- All files must be executable
- File lengths will be tested using `wc`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation must be a real sentence explaining the purpose of the module, class, or method (length will be verified)