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


class Beverage(object):
    def __init__(self):
        self.type, self.price = self.get_input()

    def save_beverage(self, user):
        if user.position == "Salesman":
            conn = sqlite3.connect('coffeeforme.db')
            c = conn.cursor()

            c.execute("INSERT INTO beverage VALUES (NULL, '{}', '{}')".format(self.type, self.price))

            ####"INSERT INTO beverage VALUES ({}, '{}', '{}','{}')".format(1, self.type, self.ingredients, self.price))
            conn.commit()

        else:
            print("Fuck you")

    def get_beverages(self, user):
        if user.position == "Salesman":
            print("Please, choose beverage to sell: \n")
            conn = sqlite3.connect('coffeeforme.db')
            c = conn.cursor()
            c.execute("SELECT * FROM beverage")
            print(c.fetchall())

    def get_input(self):
        type = input("Enter type: \n")
        price = input("Enter price: \n")
        return type, price
