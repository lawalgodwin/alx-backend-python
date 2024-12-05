#!/usr/bin/env python3
"""  Lazy loading Paginated Data
     Objective: Simulte fetching paginated data from the users database using a generator to lazily load each page
"""

import sys
from typing import Generator, Sequence
from seed import connect_to_prodev

conn = connect_to_prodev()

def paginate_users(page_size, offset):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size) -> Generator[Sequence, None, None]:
    """ Only fetch the next page when needed at an offset of 0
        Arguments:
            page_size: The number of records per page
        Returns: Generator
    """
    page_number = 1
 
    # resultset = paginate_users(page_size, offset)
    while True:
        offset = page_size * (page_number - 1)
        resultset = paginate_users(page_size, offset)
        if not resultset:
            break
        resultset = list(map(lambda user:  ({"user_id": user["user_id"], "name": user["name"], "email": user["email"], "age": int(user["age"])}), resultset))
        yield resultset
        # fetch result again
        page_number += 1
    return "No more rows to fetch"


if __name__ == "__main__":
    try:
        for page in lazy_paginate(2):
            for user in page:
                print(user)

    except BrokenPipeError:
        sys.stderr.close()
