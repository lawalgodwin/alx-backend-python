#!/usr/bin/env python3

""" This module creates a class-based context manager to handle opening and closing database connections automatically """

from mysql.connector import connect

class DatabaseConnection:
    """ context manager to handle opening and closing database connections automatically """

    def __init__(self):
        self.connection_object = connect(host='0.0.0.0', user='nedu', password='password', database='ALX_prodev')

    def __enter__(self):
        return self.connection_object

    def __exit__(self, type, value, stacktrace):
        if stacktrace:
            print(f"{type} : {value} : {stacktrace}")
        self.connection_object.close()
        return True


if __name__ == "__main__":
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        QUERY = """ SELECT * FROM user_data; """
        cursor.execute(QUERY)
        for row in cursor.fetchmany(50):
            print(row)