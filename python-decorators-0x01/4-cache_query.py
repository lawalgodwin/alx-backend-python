#!/usr/bin/env python3
""" Using decorators to cache Database Queries
    Objective: create a decorator that caches the results of a database queries in order to avoid redundant calls
"""

import time
import sqlite3 
import functools
with_db_connection = __import__("1-with_db_connection").with_db_connection

query_cache = {}

def cache_query(func):
    """ A decorator that caches the results of a database queries """
    def wrapper(*args, **kwargs):
        # before executing the function, check if the querry has been cached
        result = None
        query = kwargs.get("query")
        if not query_cache.get(query):
            result = func(*args, **kwargs)
            query_cache[query] = result # update the cache for every first call
            return result
        return query_cache.get(query) # else return the result if already in cache
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")