from Database_init import exec_insert_query, exec_select_query


def create_beverage():
    beverage = input("Enter beverage: \n")
    price = input("Enter price: \n")
    exec_insert_query("INSERT INTO beverage VALUES (NULL, '{}', '{}')".format(beverage, price))


def select_beverages():
    return exec_select_query("SELECT * FROM beverage")
