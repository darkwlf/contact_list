import sqlite3
con = sqlite3.connect('contacts.db')
cur = con.cursor()
name = input("Name : ")
num = input("Number : ")
addr = input("Address : ")
email = input("Email : ")
#cur.execute('''CREATE TABLE contact   (name, number, address, email)''')
cur.execute("INSERT INTO contact VALUES (?,?,?,?)",(name,num,addr,email))
con.commit()
#for row in cur.execute('SELECT * FROM contact ORDER BY name'):
#        print(row)
#cur.commit()
cur.close()
