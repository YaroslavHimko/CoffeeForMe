import sqlite3


def create_beverage():
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    beverage = input("Enter beverage: \n")
    price = input("Enter price: \n")
    c.execute("INSERT INTO beverage VALUES (NULL, '{}', '{}')".format(beverage, price))
    conn.commit()
    conn.close()


def select_beverages():
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute("SELECT * FROM beverage")
    conn.commit()
    available_beverages = c.fetchall()
    return available_beverages
