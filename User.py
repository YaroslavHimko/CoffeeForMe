import sqlite3
from Ingredients import create_ingredient, select_ingredient
from Beverage import create_beverage, select_beverages
from Sales import create_sale, create_bill, print_bill


class User(object):
    def __init__(self):
        self.username = input("Enter username: \n")
        self.position = input("Enter position: \n")

    def user_action(self):
        if self.position == "Manager":

            option = input(
                    "Enter 's' to show statistics\n"
                    "Enter 'u' to create new user\n"
                    "Enter 'b' to create new beverage\n"
                    "Enter 'i' to create new ingredient\n"
                    "Or q to exit:\n")
            while option != 'q':
                if option == 's':
                    user = self.get_manager_input()
                    self.statistics(user)
                    option = input("Please, choose option again:\n")
                elif option == 'u':
                    self.create_user()
                    option = input("Please, choose option again:\n")
                elif option == 'b':
                    create_beverage()
                    option = input("Please, choose option again:\n")
                elif option == 'i':
                    create_ingredient()
                    option = input("Please, choose option again:\n")

        elif self.position == "Salesman":
            if self.check_salesman():
                beverages = select_beverages()
                print("{} \n".format(beverages))
                selected_beverage = int(input("Please, choose beverage id: \n"))
                ingredients = select_ingredient()
                print("{} \n".format(ingredients))
                selected_ingredient = int(input("Please, choose ingredient id: \n"))
                order_price = float(beverages[selected_beverage - 1][2]) + float(
                        ingredients[selected_ingredient - 1][2])
                create_sale(self.username, beverages[selected_beverage - 1][1], ingredients[selected_ingredient - 1][1],
                            order_price)
                create_bill(self.username, beverages[selected_beverage - 1][1], ingredients[selected_ingredient - 1][1],
                            order_price)
            else:
                print("Please, contact your manager to register you.")

        else:
            print("Please, specify role as Manager or Salesman")

    def create_user(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        username = input("Enter user name: \n")
        position = input("Enter user position: \n")
        c.execute("INSERT INTO users VALUES (NULL,'{}','{}','{}','{}')".format(username, position, 0, 0))
        conn.commit()
        conn.close()

    def get_manager_option(self):
        option = input(
                "Enter 's' to show statistics\n"
                "Enter 'u' to create new user\n"
                "Enter 'b' to create new beverage\n"
                "Enter 'i' to create new ingredient\n"
                "Or q to exit:\n")
        return option

    def statistics(self, user):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT name, position from users WHERE name = '{}'".format(user))
        user_info = c.fetchall()
        conn.commit()
        print("Name:", user_info[0][0], "\nPosition:", user_info[0][1], "\nAmount of sales:",
              self.prepare_statistics(user)[0][0], "\nTotal value ($):", self.prepare_statistics(user)[1][0])

    def prepare_statistics(self, user):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        count = c.execute("SELECT COUNT(type) from sales WHERE username='{}'".format(user)).fetchall()
        sum_price = c.execute("SELECT SUM(price) from sales WHERE username='{}'".format(user)).fetchall()
        return count[0], sum_price[0]

    def get_manager_input(self):
        user = input("Please, enter your salesman name: \n")
        return user


    def check_salesman(self):
        conn = sqlite3.connect('coffeeforme.db')
        c = conn.cursor()
        try:
            c.execute("SELECT name from users WHERE name = '{}'".format(self.username))
            username = c.fetchone()
            conn.commit()
            return self.username == username[0]
        except TypeError:
            print("User was not found")
            return False
