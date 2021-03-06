from utils import exec_insert_query, exec_select_query, float_validator, custom_input


def create_ingredient():
    """
    Function takes input from user and executes INSERT statement to create new ingredient
    """
    ingredient = custom_input("Enter ingredient: \n")
    price = custom_input("Enter price: \n")

    if float_validator(price):
        exec_insert_query("INSERT OR IGNORE INTO ingredients VALUES (NULL, '{}', '{}')".format(ingredient, price))


def select_ingredient():
    """
    Function executes SELECT statement and gets all ingredients
    """
    return exec_select_query("SELECT * FROM ingredients")
