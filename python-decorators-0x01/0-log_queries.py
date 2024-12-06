#!/usr/bin/env python3
""" Logging database Queries
    This module cotains a decorator that logs all SQL queries run by the decorated function
    Objective: create a decorator that logs database queries executed by any function
"""

import sqlite3
import functools


def create_table():
    """ creates a table users if it does not exists with the required fields
        Arguments:
            connection: The connection object
        Returns: None
    """
    connection = sqlite3.connect('users.db')
    sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE,
                                joining_date DATETIME,
                                salary REAL NOT NULL);'''
    cursor = connection.cursor()
    cursor.execute(sqlite_create_table_query)

# cretae the users table
create_table()

#### decorator to log SQL queries

def log_queries(fn):
    """ A decorator that logs database queries before executing it """
    @functools.wraps(fn)
    def wrapper(query):
        print(query)
        fn(query)
    return wrapper
        

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

