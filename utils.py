import sqlite3


def init_db():
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute(
            """CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, position TEXT, number INTEGER, value INTEGER)""")
    c.execute(
            """CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, type TEXT, ingredient TEXT, price REAL)""")
    c.execute(
            """CREATE TABLE IF NOT EXISTS ingredients (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, type TEXT, price REAL)""")
    c.execute(
            """CREATE TABLE IF NOT EXISTS beverage (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, type TEXT, price REAL)""")
    conn.commit()
    conn.close()


def drop_db():
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute("""DROP TABLE users""")
    c.execute("""DROP TABLE beverage""")
    c.execute("""DROP TABLE ingredients""")
    c.execute("""DROP TABLE sales""")
    conn.commit()
    conn.close()


def exec_insert_query(query):
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()


def exec_select_query(query):
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute(query)
    parameter = c.fetchall()
    conn.commit()
    conn.close()
    return parameter


def float_validator(value):
    try:
        float(value)
        return True
    except ValueError:
        print("Cannot create item with price '{}'. Please, use float.".format(value))
        return False
