import sqlite3

conn = sqlite3.connect('coffeeforme.db')

c = conn.cursor()
###c.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, position TEXT)""")
c.execute("INSERT INTO users VALUES (2, 'Ann','Salesman')")
c.execute("SELECT * from users")
print(c.fetchone())