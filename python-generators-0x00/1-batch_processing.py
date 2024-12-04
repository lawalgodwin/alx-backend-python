#!/usr/bin/env python3

""" Batch processing Large Data

    This module creates a generator to fetch and process data in batches from the users database
"""

from mysql.connector import Error
from seed import connect_to_prodev

conn = connect_to_prodev()

def stream_users_in_batches(batch_size = 50):
    """ A function that fetches rows in batches

        Arguments:
            batch_size: The number of records to be fetched per batch
        Returns: list of records fetched
    """
    with conn.cursor() as cursor:
        QUERY = """ SELECT * FROM user_data """
        cursor.execute(QUERY)
        resultsets = cursor.fetchmany(batch_size)
        while resultsets:
            yield resultsets
            resultsets = cursor.fetchmany(batch_size)
            if not resultsets:
                break
            yield resultsets
               

if __name__ == "__main__":
    try:
        print(next(stream_users_in_batches(6)))
    except Error as e:
        print(e.msg)