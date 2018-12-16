import sqlite3


def create_sale(username, beverage, ingredient, order_price):
    conn = sqlite3.connect('coffeeforme.db')
    c = conn.cursor()
    print("{} {} {} {}".format(username, beverage, ingredient, order_price))
    c.execute("INSERT INTO sales VALUES (NULL, '{}', '{}', '{}', '{}')".format(username, beverage, ingredient,
                                                                               order_price))
    conn.commit()
    conn.close()


def create_bill(username, beverage, ingredients, price):
    f = open("bill.txt", "w")
    f.write("Cashier: \n{}\n============\n=============\nYou ordered {} with {} for {}".format(username, beverage,
                                                                                               ingredients, price))


def print_bill():
    f = open("bill.txt", "r")
    print(f.readline())
