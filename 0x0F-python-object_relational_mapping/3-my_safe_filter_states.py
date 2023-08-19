#!/usr/bin/python3
"""Script that tales all arguments and displays values in the
states. Make sure its safe from MySQL injections"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8")
    cursor = connection.cursor()
    try:
        query = """SELECT * FROM states WHERE name LIKE BINARY '{:s}'
        ORDER BY id ASC""".format(argv[4])
        cursor.execute(query)
        rows = cursor.fetchall()
    except MySQLdb.Error:
        try:
            tn = ("MySQLdb Error")
        except IndexError:
            tn = ("MySQLdb Error - IndexError")
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
