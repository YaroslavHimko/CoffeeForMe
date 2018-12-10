import sqlite3
import argparse


class Beverage(object):

    def __init__(self):
        args = self.get_input()
        self.type = args.type
        self.ingredients = args.ingredients
        self.price = args.price

    def file_writer(self):
        f = open("bill.txt", "w")
        f.write("Got beverage {} with {} for {}".format(self.type, self.ingredients, self.price))

    def file_reader(self):
        f = open("bill.txt", "r")
        print(f.readline())

    def db_worker(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        ###c.execute("""CREATE TABLE beverage (id INTEGER PRIMARY KEY, type TEXT, ingredients TEXT, price TEXT)""")
        c.execute(
            "INSERT INTO beverage VALUES ({}, '{}', '{}','{}')".format(1, self.type, self.ingredients, self.price))
        c.execute("SELECT * from beverage")
        print(c.fetchone())

    def get_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("type")
        parser.add_argument("ingredients")
        parser.add_argument("price")
        args = parser.parse_args()
        return args
