import sqlite3

class Ingredients(object):
    def __init__(self):
        self.type, self.price = self.get_input()

    def get_input(self):
        type = input("Enter ingredients: \n")
        price = input("Enter price: \n")
        return type, price


    def save_ingredient(self, user):
        if user.position == "Salesman":
            conn = sqlite3.connect('coffeeforme.db')
            c = conn.cursor()
            ###c.execute("""CREATE TABLE ingredients (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, type TEXT, price REAL)""")
            c.execute("INSERT INTO ingredients VALUES (NULL, '{}', '{}')".format(self.type, self.price))
            conn.commit()
        else:
            print("Fuck you")