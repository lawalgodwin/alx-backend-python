#!/usr/bin/env python3

""" Concurrent Asynchronous Database Queries
    Objective: Run multiple database queries concurrently using asyncio.gather
"""

import aiosqlite
import asyncio
from aiosqlite import Error
import sys

async def async_fetch_users():
    """ Fetch all users from the db """
    all_users = None
    db = None
    try:
        db = await aiosqlite.connect('users.db')
        cursor = await db.execute("SELECT * FROM users")
        all_users = await cursor.fetchall()
    finally:
       await db.close()       
    return all_users

async def async_fetch_older_users():
    """ Fetch users older than 40 """
    users_older_than_40 = None
    db = None
    try:
        db = await aiosqlite.connect("users.db")
        cursor = await db.execute("SELECT * FROM users WHERE aga > 40")
        users_older_than_40 = await cursor.fetchall()
    finally:
        await db.close()
    return users_older_than_40


async def fetch_concurrently():
    """ Run the async operations concurrently """
    print("running the tasks")
    try:
        result = await asyncio.gather(
            async_fetch_users(),
            async_fetch_older_users(),
            return_exceptions=True
        )
        print(result)
        return result
    except Error as e:
        error_encountered = e.with_traceback(e.__traceback__)
        print(error_encountered)
    
    print("Done !!!")

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())