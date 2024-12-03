#!/usr/bin/env python3

""" Objective: create a generator that streams rows from an SQL database one by one.
    
    Instructions: write a function that uses a generator to fetch rows one by one from the user_data table. You must use the Yield python generator
"""
from itertools import islice
from seed import connect_to_prodev

db_connection = connect_to_prodev()

def stream_users():
    """A function that fetches table rows based on request"""
    with db_connection.cursor() as cursor:
        QUERY = """ SELECT * FROM user_data; """
        cursor.execute(QUERY)
        for row in cursor.fetchall():
            user_id, name, email, age = row
            user = {"user_id": user_id, "name": name, "email": email, "age": int(age) }
            yield user


if __name__ == "__main__":
    # let's fetch the first 3 users
    for user in islice(stream_users(), 3):
        print(user)