#!/usr/bin/python3
"""Script that list all cities from the database"""
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
                charset="utf8")
        cursor = connection.cursor()
        query = """SELECT cities.id, cities.name, states.name
        FROM cities, states WHERE cities.state_id
        = states.id ORDER BY cities.id ASC"""
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)


if __name__ == "__main__":
    list_city()
