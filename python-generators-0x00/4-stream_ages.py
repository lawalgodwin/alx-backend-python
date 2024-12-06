#!/usr/bin/env python3

""" Memory-Efficient Aggregation with Generators
    Objective: to use a generator to compute a memory-efficient aggregate function i.e average age for a large dataset
    
    Instruction:

        Implement a generator stream_user_ages() that yields user ages one by one.

        Use the generator in a different function to calculate the average age without loading the entire dataset into memory

        Your script should print Average age of users: average age

        You must use no more than two loops in your script

        You are not allowed to use the SQL AVERAGE
"""

from typing import Generator
from mysql.connector import Error
from seed import connect_to_prodev

conn = connect_to_prodev()

def stream_user_ages() -> Generator:
    """ This fuction is implemented based on the instruction above"""
    cursor = conn.cursor(dictionary=True)
    QUERY = """ SELECT age FROM user_data; """
    cursor.execute(QUERY)
    user = cursor.fetchone()
    age = 0
    counter = 0
    while True:
        if not user:
            break
        age += user.get("age")
        counter += 1
        yield age
        average_age = age / counter
        print(f"Average age of users: {round(average_age, 2)}")
        user = cursor.fetchone()



if __name__ == "__main__":
    try:
        for age in stream_user_ages():
            print(age)
    except Error as e:
        print(e.msg)