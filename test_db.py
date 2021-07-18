import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

creat_table = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(creat_table)

user = ('Adi', 'asdf')

insert_query = "INSERT INTO users VALUES (?,?,?)"

users = [
    (1,"Hanna", "ewrwe"),
    (2,"Jules", "ewewd"),
    (3,"Mark", "rrrwwnd")
    ]
try:
    cursor.executemany(insert_query, users)
    
    
    
    
    select_query = "SELECT * FROM users"
    
    for row in cursor.execute(select_query):
        print(row)
finally:
    connection.commit()
    connection.close()
