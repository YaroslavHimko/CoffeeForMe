import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("position")
parser.add_argument("type")
parser.add_argument("ingredients")
parser.add_argument("price")
args = parser.parse_args()


class User(object):
    def __init__(self):
        self.username = args.username
        self.position = args.position


class Beverage(object):
    def __init__(self):
        self.type = args.type
        self.ingredients = args.ingredients
        self.price = args.price

    def file_writer(self):
        f = open("bill.txt", "w")
        f.write("Got beverage {} with {} for {}".format(self.type, self.ingredients, self.price))

    def file_reader(self):
        f = open("bill.txt", "r")
        print(f.readline())


user = User()
beverage = Beverage()

beverage.file_writer()
beverage.file_reader()


conn = sqlite3.connect('coffeeforme.db')

c = conn.cursor()
###c.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, position TEXT)""")
c.execute("INSERT INTO users VALUES ({}, '{}','{}')".format(1, user.username, user.position))
c.execute("SELECT * from users")
print(c.fetchone())
