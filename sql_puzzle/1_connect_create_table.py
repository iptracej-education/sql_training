import sqlite3
conn = sqlite3.connect('mydata.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXIST users(id INTEGER PRIMARY KEY, name TEXT)")
cur.insert("INSERT INTO users (name) VALUES (?)", ("ALICE",))
conn.commit()

for row in cur.execute("SELECT * FROM users"):
    print(row)
    
conn.close()

