#!/usr/bin/python3
"""Script that tales all arguments and displays values in the
states. Make sure its safe from MySQL injections"""
import MySQLdb
from sys import argv


def list_state():
    try:
        connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                charset="utf8")
        cursor = connection.cursor()
        query = """SELECT * FROM states WHERE name LIKE BINARY '{:s}'
        ORDER BY id ASC""".format(argv[4])
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    list_state()
