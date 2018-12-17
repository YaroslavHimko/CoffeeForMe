from utils import exec_insert_query


def create_sale(username, beverage, ingredient, order_price):
    """
    Function takes username, beverage, ingredient, order_price parameters and executes
    INSERT statement to create new sale record
    """
    print("{} {} {} {}".format(username, beverage, ingredient, order_price))
    exec_insert_query("INSERT INTO sales VALUES (NULL, '{}', '{}', '{}', '{}')".format(username, beverage, ingredient,
                                                                                       order_price))


def create_bill(username, beverage, ingredients, price):
    """
    Function creates or overrides text file with bill for client.
    Function takes username, beverage, ingredient, order_price parameters.
    """
    f = open("bill.txt", "w")
    f.write("Cashier: {}. You ordered {} with {} for {}".format(username, beverage,
                                                                ingredients, price))


def print_bill():
    """
    Function used for printing bill to a client.
    Currently implemented with print function
    """
    f = open("bill.txt", "r")
    print(f.readlines())
