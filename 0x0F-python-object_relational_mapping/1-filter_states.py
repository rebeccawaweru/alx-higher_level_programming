#!/usr/bin/python3
"""Script that lists all states with a name starting with N from db"""
import MySQLdb
from sys import argv


def list_states():
    try:
        connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                charset="utf8")
        cursor = connection.cursor()
        query = """SELECT * FROM states WHERE
        name LIKE BINARY 'N%' ORDER BY id ASC"""
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except MySQLdb.Error:
        print("MySQL Error")


if __name__ == "__main__":
    list_states()
