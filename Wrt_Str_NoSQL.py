"""
This script stores and reads data from txt file.
"""


def store(extraction):
    """Stores the data in a txt file"""
    with open("data.txt", "a") as file:
        file.write(extraction + "\n")


def read():
    """Reads the data stored in the txt"""
    with open("data.txt", "r") as file:
        return file.read()
