import sqlite3
from Ingredients import create_ingredient, select_ingredient
from Beverage import create_beverage, select_beverages
from Sales import create_sale, create_bill, print_bill


class User(object):
    def __init__(self):
        self.username, self.position = self.get_input()

    def check_role(self):
        if self.position == "Manager":
            option = input(
                    "Enter 's' to show statistics\nEnter 'u' to create new user\nEnter 'b' to create new beverage\nEnter 'i' to create new ingredient:\n")
            if option == 's':
                user = self.get_manager_input()
                self.statistics(user)
            elif option == 'u':
                self.create_user()
            elif option == 'b':
                create_beverage()
            elif option == 'i':
                create_ingredient()

        else:
            beverages = select_beverages()
            print("{} \n".format(beverages))
            selected_beverage = int(input("Please, choose beverage id: \n"))
            ingredients = select_ingredient()
            print("{} \n".format(ingredients))
            selected_ingredient = int(input("Please, choose ingredient id: \n"))
            order_price = float(beverages[selected_beverage - 1][2]) + float(ingredients[selected_ingredient - 1][2])
            create_sale(self.username, beverages[selected_beverage - 1][1], ingredients[selected_ingredient - 1][1],
                        order_price)
            create_bill(self.username, beverages[selected_beverage - 1][1], ingredients[selected_ingredient - 1][1],
                        order_price)

    def create_user(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        username = input("Enter user name: \n")
        position = input("Enter user position: \n")
        c.execute("INSERT INTO users VALUES (NULL,'{}','{}','{}','{}')".format(username, position, 0, 0))
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

    def execute_query(self, exec_string):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        c.execute(exec_string)
        conn.commit()
        conn.close()
