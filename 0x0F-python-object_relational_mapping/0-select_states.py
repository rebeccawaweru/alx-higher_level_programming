#!/usr/bin/python3
""" script that lists all states from database"""
import MySQLdb
from sys import argv


def list_states():
    try:
        """Connect to the MySQL server"""
        connection = MySQLdb.connect(
                host="localhost",
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                port=3306,
                charset="utf8"
        )
        """Create cursor to execute SQL queries"""
        cursor = connection.cursor()

        """Execute the SELECT query"""
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        """Fetch all rows"""
        rows = cursor.fetchall()

        """Display the results"""
        for row in rows:
            print(row)

        """Close the cursor and connection"""
        cursor.close()
        connection.close

    except MySQLdb.Error:
        print("MySQLdb Error")


if __name__ == "__main__":
    list_states()
