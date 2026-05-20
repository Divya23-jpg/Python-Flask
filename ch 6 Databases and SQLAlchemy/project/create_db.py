import sqlite3

# ! Open and use site.db if not
conn=sqlite3.connect('site.db')

# ! allows to send data to databse
cursor=conn.cursor()
# ! Create table users with column
cursor.execute('''CREATE TABLE users
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL )'''
)
# ! to commit chnages
conn.commit()

conn.close()
