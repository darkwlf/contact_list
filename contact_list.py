import sqlite3
con = sqlite3.connect('contacts.db')
cur = con.cursor()
for row in cur.execute('SELECT * FROM contact ORDER BY name'):
        print(row)

