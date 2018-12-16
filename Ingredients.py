import sqlite3


def create_ingredient():
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    ingredient = input("Enter ingredient: \n")
    price = input("Enter price: \n")
    c.execute("INSERT INTO ingredients VALUES (NULL, '{}', '{}')".format(ingredient, price))
    conn.commit()
    conn.close()


def select_ingredient():
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ingredients")
    conn.commit()
    available_ingredients = c.fetchall()
    return available_ingredients
