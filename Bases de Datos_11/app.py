import sqlite3

conn = sqlite3.connect('main.db')

cursor = conn.cursor()
rows = cursor.execute('SELECT * FROM users;')

for row in rows:
    print(row)

#conn.commit() cuando realizamos operaciones tipo INSERT, DELETE
cursor.close()
conn.close()


