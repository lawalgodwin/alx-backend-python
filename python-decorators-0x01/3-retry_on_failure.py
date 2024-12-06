#!/usr/bin/env python3
""" Using Decorators to retry database queries
    Objective: create a decorator that retries database operations if they fail due to transient errors
"""

import time
import sqlite3 
import functools

with_db_connection = __import__("1-with_db_connection").with_db_connection

def retry_on_failure(retries=0, delay=0):
    """ A decorator factory
    """
    def decorator(func):
        """ A decorator that retries database operations if they fail due to transient errors """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception:
                # retry due to transient error
                for i in range(retries):
                    print(f"Retrying......{i + 1}")
                    try:
                        result = func(*args, **kwargs)
                        if (result):
                            break
                    except Exception as error:
                        print("Error occured: ", error)
                        result = error
                    time.sleep(delay)
            return result
        return wrapper
    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)