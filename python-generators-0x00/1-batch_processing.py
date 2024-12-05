#!/usr/bin/env python3

""" Batch processing Large Data

    This module creates a generator to fetch and process data in batches from the users database
"""

from mysql.connector import Error, connect
from seed import connect_to_prodev
from typing import Generator

conn = connect_to_prodev()

def stream_users_in_batches(batch_size = 50) -> Generator[int, None, str]:
    """ A function that fetches rows in batches

        Arguments:
            batch_size: The number of records to be fetched per batch
        Returns: Generator
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
    cursor.close()
    conn.close()
    return "No more rows to fetch"


def batch_processing(batch_size) -> None:
    """ A function that processes each batch to filter users over the age of 25
        Arguments:
            batch_size: the number of batches to be processed
        Returns: None
    """
    batch = next(stream_users_in_batches(batch_size))
    if not batch:
        return print("No row to fetch")
    users_above_25 =list(filter(lambda row: (int(row["age"]) > 25), batch))
    for user in users_above_25:
        user.update({"age": int(user["age"])})
        print("\n", user, end="\n\n")


if __name__ == "__main__":
    try:
        batch_processing(6)
    except Error as e:
        print(e.value)