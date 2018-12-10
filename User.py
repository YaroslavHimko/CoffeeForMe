import sqlite3
import argparse


class User(object):

    def __init__(self):
        args = self.get_input()
        self.username = args.username
        self.position = args.position

    def db_worker(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        ###c.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, position TEXT)""")
        c.execute("INSERT INTO users VALUES ({}, '{}','{}')".format(1, self.username, self.position))
        c.execute("SELECT * from users")
        print(c.fetchone())

    def get_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("username")
        parser.add_argument("position")
        args = parser.parse_args()
        return args
