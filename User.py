from Ingredients import create_ingredient, select_ingredient
from Beverage import create_beverage, select_beverages
from Sales import create_sale, create_bill, print_bill
from utils import exec_insert_query, exec_select_query


class User(object):
    def __init__(self):
        self.username = input("Enter username: \n")
        self.position = input("Enter position (Manager/Salesman): \n")

    def user_action(self):
        if self.position == "Manager":
            self.get_manager_option()
        elif self.position == "Salesman":
            if self.check_salesman():
                beverages = select_beverages()
                print("{} \n".format(beverages))
                selected_beverage = int(input("Please, choose beverage id: \n"))
                print(selected_beverage)
                ingredients = select_ingredient()
                print("{} \n".format(ingredients))
                selected_ingredient = int(input("Please, choose ingredient id: \n"))
                print(selected_ingredient)

                user, beverage, ingredient, price = self.process_sale(beverages, selected_beverage, ingredients,
                                                                      selected_ingredient)
                create_sale(user, beverage, ingredient, price)
                create_bill(user, beverage, ingredient, price)
                print_bill()
            else:
                print("Please, contact your manager to register you.")

        else:
            print("Please, specify role as Manager or Salesman")

    @staticmethod
    def create_user():
        username = input("Enter user name: \n")
        position = input("Enter user position (Manager/Salesman): \n")
        if position == "Salesman" or position == "Manager":
            exec_insert_query(
                    "INSERT OR IGNORE INTO users VALUES (NULL,'{}','{}','{}','{}')".format(username, position, 0, 0))
        else:
            print("Incorrect position '{}'.\nYou should specify position 'Manager' or 'Salesman'".format(position))

    def get_manager_option(self):
        option = input(
                "Enter 's' to show statistics\n"
                "Enter 'u' to create new user\n"
                "Enter 'b' to create new beverage\n"
                "Enter 'i' to create new ingredient\n"
                "Or q to exit:\n")
        if option == 's':
            user = self.get_manager_input()
            self.statistics(user)
            self.get_manager_option()
        elif option == 'u':
            self.create_user()
            self.get_manager_option()
        elif option == 'b':
            create_beverage()
            self.get_manager_option()
        elif option == 'i':
            create_ingredient()
            self.get_manager_option()
        elif option == 'q':
            return
        else:
            print("'{}' option is not supported.".format(option))
            self.get_manager_option()
        return option

    def statistics(self, user):
        user_info = exec_select_query("SELECT DISTINCT name, position from users WHERE name = '{}'".format(user))
        try:
            name = user_info[0][0]
            position = user_info[0][1]
            amount = self.prepare_statistics(user)[0][0]
            total_value = self.prepare_statistics(user)[1][0]

            print("Name: {}\nPosition: {}\nAmount of sales: {}\nTotal value ($): {}\n".format(name, position, amount,
                  total_value))
            exec_insert_query("UPDATE users SET number='{}', value='{}' WHERE name='{}';".format(amount, total_value, user))
        except IndexError:
            print("User doesn't exist")

    @staticmethod
    def prepare_statistics(user):
        count = exec_select_query("SELECT COUNT(type) from sales WHERE username='{}'".format(user))
        sum_price = exec_select_query("SELECT SUM(price) from sales WHERE username='{}'".format(user))
        return count[0], sum_price[0]

    @staticmethod
    def get_manager_input():
        user = input("Please, enter your salesman name: \n")
        return user

    def check_salesman(self):
        try:
            username = exec_select_query("SELECT name from users WHERE name = '{}'".format(self.username))
            return self.username == username[0][0]
        except (TypeError, IndexError):
            print("User was not found")
            return False

    @staticmethod
    def calculate_sale_price(beverages, selected_beverage, ingredients, selected_ingredient):
        order_price = float(beverages[selected_beverage - 1][2]) + float(
                ingredients[selected_ingredient - 1][2])
        return order_price

    def process_sale(self, beverages, selected_beverage, ingredients, selected_ingredient):
        order_price = self.calculate_sale_price(beverages, selected_beverage, ingredients, selected_ingredient)
        return self.username, beverages[selected_beverage - 1][1], ingredients[selected_ingredient - 1][1], order_price
