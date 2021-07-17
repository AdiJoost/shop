import sqlite3
from models.user_model import UserModel

class Database():
    def __init__(self):
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        creat_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text UNIQUE, password text)"
        try:
            cursor.execute(creat_table)
            connection.commit()
            print("Created users-Table")
        except:
            print("Table users probably already exists")
        finally:
            connection.close()
            
    
    def get_user_by_id(self, id_):
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        search_query = "SELECT * FROM users WHERE id = (?)"
        for row in cursor.execute(search_query, (id_,)):
            connection.commit()
            connection.close()
            return UserModel(row[0], row[1], row[2])
        connection.commit()
        connection.close()
        return None
    
    def get_user_by_username(self, username):
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        search_query = "SELECT * FROM users WHERE username = (?)"
        
        for row in cursor.execute(search_query, (username,)):
            connection.commit()
            connection.close()
            return UserModel(row[0], row[1], row[2])
        
        connection.commit()
        connection.close()
        return None
    
    def insert_user(self, username, password):
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        insert_query = "INSERT INTO users VALUES (?,?,?)"
        user = (None, username, password)
        try:
            cursor.execute(insert_query, user)
            connection.commit()
            connection.close()
            return True
        except:
            print("Insertion failed")
            connection.commit()
            connection.close()
            return False
        
    def get_all_users(self):
        connection = sqlite3.connect('user_database.db')
        cursor = connection.cursor()
        search_query = "SELECT * FROM users"
        users = []
        for row in cursor.execute(search_query):
            users.append(row)
        connection.commit()
        connection.close()
        return users