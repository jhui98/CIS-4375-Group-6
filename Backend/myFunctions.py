# @wakindo
#====================================================
# Implement all functions we may need to re-use here
#====================================================

# SQL and DB access functions
import mysql.connector
from mysql.connector import Error

# function used to create a connection to the DB
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB was successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# function used to execute a W query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# function used to execute a read only query
def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")






#####################################################################
#                    NOTES & REFERENCES                            #
#####################################################################
# CIS3368 Lectures with Prof. Otto / Fall 22
# https://dev.mysql.com/doc/
# https://stackoverflow.com/
# https://www.geeksforgeeks.org/
# https://pynative.com/
#================================================================
#       CIS4375 - Group 6 - SPring 23 @ All rights reserved     #
#================================================================






