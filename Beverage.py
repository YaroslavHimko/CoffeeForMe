from utils import exec_insert_query, exec_select_query, float_validator, custom_input


def create_beverage():
    beverage = custom_input("Enter beverage: \n")
    price = custom_input("Enter price: \n")
    if float_validator(price):
        exec_insert_query("INSERT OR IGNORE INTO beverage VALUES (NULL, '{}', '{}')".format(beverage, price))


def select_beverages():
    return exec_select_query("SELECT * FROM beverage")
