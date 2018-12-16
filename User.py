import sqlite3
import argparse


class User(object):

    def __init__(self):
        self.username, self.position = self.get_input()

    def check_role(self):
        if self.position == "Manager":
            while (input("Do you want to show statistics? y/n \n") != 'n'):
                user = self.get_manager_input()
                self.statistics(user)
                conn = sqlite3.connect('coffeeforme.db')
                c = conn.cursor()

                conn.commit()
        else:
            beverages = self.select_beverages()
            print("{} \n".format(beverages))
            selected_beverage = int(input("Please, choose beverage id: \n"))
            ingredients = self.select_ingredient()
            print("{} \n".format(ingredients))
            selected_ingredient = int(input("Please, choose ingredient id: \n"))
            order_price = beverages[selected_beverage - 1][2] + ingredients[selected_ingredient - 1][2]
            self.insert_sale(beverages[selected_beverage - 1][1], ingredients[selected_ingredient - 1][1], order_price)



    def create_db(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        ###c.execute("""DROP TABLE users""")
        ###c.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, position TEXT, number INTEGER, value INTEGER)""")
        c.execute("INSERT INTO users VALUES (NULL,'{}','{}','{}','{}')".format(self.username, self.position, 0, 0))
        conn.commit()
        ###c.execute("SELECT * from users")
        ###print(c.fetchone())
        ###conn.commit()

    def select_ingredient(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        c.execute("SELECT * from ingredients")
        conn.commit()
        available_ingredients = c.fetchall()
        return available_ingredients

    def select_beverages(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        c.execute("SELECT * from beverage")
        conn.commit()
        available_beverages = c.fetchall()
        return available_beverages

    def create_sales_db(self, user):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE sales (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, type TEXT, ingredient TEXT, price REAL)""")
        conn.commit()

    def insert_sale(self, beverage, ingredient, order_price):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        print("{} {} {} {}".format(self.username, beverage, ingredient, order_price))
        c.execute("INSERT INTO sales VALUES (NULL, '{}', '{}', '{}', '{}')".format(self.username, beverage, ingredient, order_price))
        conn.commit()
        conn.close()

    def statistics(self, user):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        c.execute("SELECT name, position from users WHERE name = '{}'".format(user))
        user_info = c.fetchall()
        conn.commit()
        print(user_info, self.prepare_statistics(user))


    def prepare_statistics(self, user):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        count = c.execute("SELECT COUNT(type) from sales WHERE username='{}'".format(user)).fetchall()
        sum_price = c.execute("SELECT SUM(price) from sales WHERE username='{}'".format(user)).fetchall()
        return count, sum_price

    def get_manager_input(self):
        user = input("Please, enter your salesman name: \n")
        return user

    def get_input(self):
        position = input("Enter position: \n")
        username = input("Enter username: \n")
        return username, position
