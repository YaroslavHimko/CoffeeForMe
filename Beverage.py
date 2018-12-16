import sqlite3
import argparse
import User

class Beverage(object):

    def __init__(self):
        self.type, self.price = self.get_input()

    def file_writer(self):
        f = open("bill.txt", "w")
        f.write("Got beverage {} for {}".format(self.type, self.price))

    def file_reader(self):
        f = open("bill.txt", "r")
        print(f.readline())

    def save_beverage(self, user):
        if user.position == "Salesman":
            conn = sqlite3.connect('coffeeforme.db')
            c = conn.cursor()
            ###c.execute("""DROP TABLE beverage""")
            ###c.execute("""CREATE TABLE beverage (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, type TEXT, price REAL)""")

            c.execute("INSERT INTO beverage VALUES (NULL, '{}', '{}')".format(self.type, self.price))

            ###c.execute(
                ####"INSERT INTO beverage VALUES ({}, '{}', '{}','{}')".format(1, self.type, self.ingredients, self.price))
            conn.commit()

        else:
            print("Fuck you")

    def get_beverages(self, user):
        if user.position == "Salesman":
            print("Please, choose beverage to sell: \n")
            conn = sqlite3.connect('coffeeforme.db')
            c = conn.cursor()
            c.execute("SELECT * from beverage")
            print(c.fetchall())

    def get_input(self):
        type = input("Enter type: \n")
        price = input("Enter price: \n")
        return type, price
