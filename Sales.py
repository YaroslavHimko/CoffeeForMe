from utils import exec_insert_query


def create_sale(username, beverage, ingredient, order_price):
    print("{} {} {} {}".format(username, beverage, ingredient, order_price))
    exec_insert_query("INSERT INTO sales VALUES (NULL, '{}', '{}', '{}', '{}')".format(username, beverage, ingredient,
                                                                                       order_price))


def create_bill(username, beverage, ingredients, price):
    f = open("bill.txt", "w")
    f.write("Cashier: {}. You ordered {} with {} for {}".format(username, beverage,
                                                                ingredients, price))


def print_bill():
    f = open("bill.txt", "r")
    print(f.readlines())
