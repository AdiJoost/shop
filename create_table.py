import sqlite3


def create_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    create_table_users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    cursor.execute(create_table_users)
    
    
    create_table_items = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL)"
    cursor.execute(create_table_items)
    
    
    
    connection.commit()
    connection.close()