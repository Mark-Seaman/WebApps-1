# Lesson 2 - Installing Python 3 and Visual Studio

## Install Visual Studio Code
- Install Visual Studio Code
    - https://code.visualstudio.com 
    - Download and run installer
- Install Python extension


## Install Python 3

Install from https://www.python.org/

Setup command path for Python

    $ python --version  

Should be Python 3.10 or better


## Setup Virtual Env
Create and activate a virtual environment if you want to isolate your work from other python projects on your computer.

    $ python -m venv venv

    $ source venv/bin/activate   # On Mac
    $ .\venv\Scripts\activate.bat    # On Windows

If it doesn't work right away then use the installed version.


## Run Test Program

Check your Python path and version

    cd 02
    python test.py

