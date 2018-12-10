import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("position")
args = parser.parse_args()


class User(object):
    def __init__(self):
        self.username = args.username
        self.position = args.position


user = User()

conn = sqlite3.connect('coffeeforme.db')

c = conn.cursor()
###c.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, position TEXT)""")
c.execute("INSERT INTO users VALUES ({}, '{}','{}')".format(1, user.username, user.position))
c.execute("SELECT * from users")
print(c.fetchone())
