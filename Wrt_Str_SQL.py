"""
This script stores and reads data from SQL file.
"""
import sqlite3 as sq

# Opens a connections into a data base file
connection = sq.connect("data.db")


def store(extraction):
    """Stores the data in a txt file"""

    row = extraction.split(",")
    row = [items.strip() for items in row]

    # Access the data inside the database
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?,?,?)", row)

    connection.commit()


def read(extracted):
    """Reads the data stored in the txt"""
    row = extracted.split(",")
    row = [items.strip() for items in row]

    # Access the data inside the database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", row)
    data = cursor.fetchall()
    return data


if __name__ == "__main__":
    store("Feng Suave, Minimalia City, 5.5.2089")