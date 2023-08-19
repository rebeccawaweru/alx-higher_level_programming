#!/usr/bin/python3
"""Script that takes in the name of state as argument
and list all cities"""
import MySQLdb
from sys import argv


def list_city():
    try:
        connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                charset="utf8"
                )
        cursor = connection.cursor()
        arg = argv[4]
        query = """
        SELECT cities.name FROM cities WHERE
        cities.state_id LIKE BINARY
        (SELECT states.id FROM states WHERE
        states.name LIKE BINARY %s) ORDER BY cities.id ASC
        """
        cursor.execute(query, (arg,))
        rows = cursor.fetchall()
        arry = []
        for row in rows:
            arry += row
        print(", ".join(arry))
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)


if __name__ == "__main__":
    list_city()
