#!/usr/bin/env python3

""" This module creates a reusable context manager that takes a query as input and executes it, managing both connection and the query execution
"""

# from mysql.connector import connect, Error
import sqlite3
from sqlite3 import Error

class ExecuteQuery:
    """ A reusable context manager that manages both DB connection and the query execution
        Arguments:
            query: The parameterized query to be execcuted
            param: The param to be used by the query
        Returns: The query results
    """

    def __init__(self, query="SELECT * FROM user_data WHERE age > ?", params=25):
        self.connection_object = sqlite3.connect('users.db')
        self.query = query
        self.param = params

    def __enter__(self):
        cursor = self.connection_object.cursor()
        result = None
        try:
            cursor.execute(self.query, self.param)
            result = cursor.fetchall()
        except Error as e:
            print(e.with_traceback(e.__traceback__))
        return result if result else []

    def __exit__(self, type, value, stacktrace):
        if stacktrace:
            print(f"{type} : {value}")
        self.connection_object.close()
        return False


if __name__ == "__main__":
    with ExecuteQuery("SELECT * FROM users WHERE age > ?", 50) as query_result:
        for row in query_result:
            print(row)