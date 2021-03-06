from __future__ import print_function
import sqlite3


def init_db():
    """
    Function creates database and its tables.
    Used for the first application's run
    """
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute(
            """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT, position TEXT, number INTEGER, value INTEGER, UNIQUE(name))""")
    c.execute(
            """CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username TEXT, type TEXT, ingredient TEXT, price REAL)""")
    c.execute(
            """CREATE TABLE IF NOT EXISTS ingredients (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type TEXT, price REAL, UNIQUE(type))""")
    c.execute(
            """CREATE TABLE IF NOT EXISTS beverage (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                type TEXT, price REAL, UNIQUE (type))""")
    conn.commit()
    conn.close()


def drop_db():
    """
    Function for clearing database from test records
    """
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute("""DROP TABLE users""")
    c.execute("""DROP TABLE beverage""")
    c.execute("""DROP TABLE ingredients""")
    c.execute("""DROP TABLE sales""")
    conn.commit()
    conn.close()


def exec_insert_query(query):
    """
    Function create connection to a database,
    create cursor, execute query, commits and closes connection.
    Function takes query as a string parameter.
    """
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def exec_select_query(query):
    """
    Function create connection to a database,
    create cursor, execute query, commits and closes connection.
    Unlike insert function, select function perform fetchall.
    Function takes query as a string parameter.
    """
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute(query)
    parameter = c.fetchall()
    conn.commit()
    conn.close()
    return parameter


def float_validator(value):
    """
    Function used as a validator to not allow user perform unacceptable inputs.
    """
    try:
        float(value)
        return True
    except ValueError:
        print("Cannot create item with price '{}'. Please, use float.".format(value))
        return False


def fill_db():
    """
    Function used as a filler for a database.
    Created mostly for presentation.
    """
    exec_insert_query("INSERT OR IGNORE INTO ingredients VALUES (NULL, '{}', '{}')".format("Sugar", 0.0))
    exec_insert_query("INSERT OR IGNORE INTO ingredients VALUES (NULL, '{}', '{}')".format("Chocolate", 0.3))
    exec_insert_query("INSERT OR IGNORE INTO ingredients VALUES (NULL, '{}', '{}')".format("Milk", 1.0))
    exec_insert_query("INSERT OR IGNORE INTO ingredients VALUES (NULL, '{}', '{}')".format("Cap", 0.1))
    exec_insert_query("INSERT OR IGNORE INTO ingredients VALUES (NULL, '{}', '{}')".format("Cinnamon", 0.0))

    exec_insert_query("INSERT OR IGNORE INTO beverage VALUES (NULL, '{}', '{}')".format("Americano", 2.5))
    exec_insert_query("INSERT OR IGNORE INTO beverage VALUES (NULL, '{}', '{}')".format("RAF", 4.5))
    exec_insert_query("INSERT OR IGNORE INTO beverage VALUES (NULL, '{}', '{}')".format("Cappuccino", 4.0))
    exec_insert_query("INSERT OR IGNORE INTO beverage VALUES (NULL, '{}', '{}')".format("Latte", 4.0))
    exec_insert_query("INSERT OR IGNORE INTO beverage VALUES (NULL, '{}', '{}')".format("Espresso", 3.0))
    exec_insert_query("INSERT OR IGNORE INTO beverage VALUES (NULL, '{}', '{}')".format("Tea", 1.5))


def custom_input(value):
    """
    Function solves compatibility issue regarding input methods in Python 2.7 and Python 3+
    """
    try:
        input = raw_input
        return input(value)
    except NameError:
        pass
