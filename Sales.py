import sqlite3

class Sales(object):
    def __init__(self):
        pass


    def create_db(self, user):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE sales (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, type TEXT, ingredient TEXT, price REAL)""")
        ###c.execute("INSERT INTO sales VALUES (NULL, '{}', '{}', '{}', '{}')".format(user.username, self.type, self.ingredient, self.price))
        conn.commit()