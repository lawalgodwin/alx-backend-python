#!/usr/bin/env python3

""" Batch processing Large Data

    This module creates a generator to fetch and process data in batches from the users database
"""

from mysql.connector import Error, connect
# from seed import connect_to_prodev

conn = connect(host="0.0.0.0", user="nedu", password="password", database="ALX_prodev")

def stream_users_in_batches(batch_size = 50):
    """ A function that fetches rows in batches

        Arguments:
            batch_size: The number of records to be fetched per batch
        Returns: list of records fetched
    """
    cursor = conn.cursor(dictionary=True)
    QUERY = """ SELECT * FROM user_data """
    cursor.execute(QUERY)
    rows =  cursor.fetchmany(batch_size)
    while True:
        if not rows:
            break
        yield rows
        rows = cursor.fetchmany(batch_size)
    return "No more rows to fetch"


if __name__ == "__main__":
    try:
        print(next(stream_users_in_batches(2)))
    except Error as e:
        print(e.value)