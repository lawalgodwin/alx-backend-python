#!/usr/bin/env python3

""" Handle Database Connections with a Decorator
    Objective: create a decorator that automatically handles opening and closing database connections
"""


import sqlite3 
import functools

def with_db_connection(func):
    """ A decorator that automatically handles opening and closing database connections """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # open connection
            print("About making connection")
            conn = sqlite3.connect('users.db')
            result = func(conn, *args, **kwargs)
            return result
        finally:
            # close connection
            if conn:
                conn.close()
            print("connection clased")
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
    return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)