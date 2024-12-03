#!/usr/bin/env python3

""" Getting started with python generators
    Objective: Set up the database, tables and seed the databse.
"""

from mysql.connector import connect
from mysql.connector import MySQLConnection, Error
import csv


database_config = { "host": "0.0.0.0", "user": "nedu", "password": "password"}

def connect_db() -> MySQLConnection | None:
    """ connects to the mysql database server 
        Arguments: None
        Returns: MysqlDB connection object
    """

    connection = None
    try:
        connection = connect(**database_config)
        return connection
    except Error as e:
        print(f"Error making connection: {e.msg}")
        return None


def create_database(connection: MySQLConnection) -> None:
    """ creates the database ALX_prodev if it does not exist
        Arguments:
            connection: The MysqlDB connection object
        Returns: None
    """
    DB_CREATE_QUERY = """ CREATE DATABASE IF NOT EXISTS ALX_prodev; """
    cursor = connection.cursor()
    cursor.execute(DB_CREATE_QUERY)


def connect_to_prodev() -> MySQLConnection | None:
    """ connects the the ALX_prodev database in MYSQL
        Returns: MySQLConnection object
    """
    database_config["database"] = "ALX_prodev"
    connection = None
    try:
        connection = connect(**database_config)
        return connection
    except Error as e:
        print(f"Error making connection: {e.msg}")
        return None


def create_table(connection: MySQLConnection):
    """ creates a table user_data if it does not exists with the required fields
        Arguments:
            connection: The connection object
        Returns: None
    """
    TABLE_CREATE_QUERY = """
                            CREATE TABLE IF NOT EXISTS user_data
                            (
                                user_id CHAR(36),
                                name VARCHAR(36) NOT NULL,
                                email VARCHAR(100) NOT NULL,
                                age DECIMAL NOT NULL,
                                KEY idx_user_id (user_id),
                                PRIMARY KEY (user_id)
                            );
                        """
    with connection.cursor() as cursor:
        cursor.execute(TABLE_CREATE_QUERY)
        # connection.commit()


def insert_data(connection: MySQLConnection, data):
    """ inserts data in the database if it does not exist
        Arguments:
            connection: The connection object
            data: The data source(a file)
        Returns: Mysql Cursor object
    """
    with connection.cursor() as cursor:
        with open(data) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            print(f"Our database is {connection.database}")
            row_number = 0
            for row in csv_reader:
                if row_number == 0:
                    row_number += 1
                    continue
                # print(f"{str(row[0])}, {str(row[1])}, {str(row[2])}, {row[3]}")
                INSERT_SCRIPT = f""" INSERT INTO user_data (user_id, name, email, age) 
                                    VALUES 
                                    ('{row[0]}', '{row[1]}', '{row[2]}', {row[3]}) """
                try:
                    cursor.execute(INSERT_SCRIPT)
                    connection.commit()
                    print(f"Sucessfully inserted user {row[0]}")
                except Error as e:
                    print("Unable to insert ", e.msg)

    return cursor



if __name__ == "__main__":
    cnx = connect_db()

    create_database(cnx)
    cnx.close()

    con = connect_to_prodev()
    print(con.is_connected())

    create_table(con)

    insert_data(con, 'user_data.csv')
