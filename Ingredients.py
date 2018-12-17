from utils import exec_insert_query, exec_select_query, float_validator


def create_ingredient():
    ingredient = input("Enter ingredient: \n")
    price = input("Enter price: \n")

    if float_validator(price):
        exec_insert_query("INSERT INTO ingredients VALUES (NULL, '{}', '{}')".format(ingredient, price))


def select_ingredient():
    return exec_select_query("SELECT * FROM ingredients")
