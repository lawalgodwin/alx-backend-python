#!/usr/bin/env python3

""" Transaction Management Decorator
    Objective: create a decorator that manages database transactions by automatically committing or rolling back changes
"""

import sqlite3 
import functools
db = __import__('1-with_db_connection')

def transactional(func):
    """ A decorator that manages database transactions by automatically committing or rolling back changes """
    print("Running transactional decorator")
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            # commit changes
            conn.commit()
            return result
        except Exception as e:
            # rollback changes
            print("An exception ocurred...Rolling back changes...", e)
            conn.rollback()
    return wrapper

@db.with_db_connection
@transactional 
def update_user_email(conn, user_id, new_email):
    print("Executing function....") 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    print("Done executing function...")

#### Update user's email with automatic transaction handling 
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')